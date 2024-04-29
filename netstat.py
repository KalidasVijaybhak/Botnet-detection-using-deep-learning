import pandas as pd
import statistics
from scapy.all import *
import keras
import numpy as np
from sklearn.preprocessing import StandardScaler
class PcapToCsvConverter:
    def __init__(self, pcap_file, csv_output,model_path):
        self.pcap_file = pcap_file
        self.csv_output = csv_output
        self.model_path = model_path 
        

    def convert(self):
        packets = rdpcap(self.pcap_file)  # Read the pcap file
        flow_data = self._process_packets(packets)
        flow_features = self._calculate_features(flow_data,packets)
        pred = self._make_predictions(flow_features)
        self._write_to_csv(flow_features)
        self._append_predictions_to_file(pred)

    def _process_packets(self,  packets):
        flow_data = {}
        for packet in  packets:
           if IP in packet and (TCP in packet or UDP in packet):  # Check for IP and either TCP or UDP
                # Key for flow identification
                flow_key = (packet[IP].src, packet[IP].dst, packet[IP].proto, packet.sport, packet.dport)
                
                if flow_key not in flow_data:
                    flow_data[flow_key] = {
                        'timestamps': [packet.time],  # Initialize list with first timestamp
                        'lengths': [len(packet)],  # Initialize list with first packet length
                        'syn_count': 1 if TCP in packet and packet[TCP].flags & 0x02 else 0  # Count SYN flag if TCP packet
                    }
                else:
                    flow_data[flow_key]['timestamps'].append(packet.time)
                    flow_data[flow_key]['lengths'].append(len(packet))
                    if TCP in packet and packet[TCP].flags & 0x02:
                        flow_data[flow_key]['syn_count'] += 1
        return flow_data

    def _calculate_features(self, flow_data,packets):
        flow_features = {}
        for flow_key, data in flow_data.items():
            flow_features = {
            'Fwd Pkts/s': [],
            'Flow Pkts/s': [],
            'Bwd Pkts/s': [],
            'Init Bwd Win Byts': [],
            'Active Min': [],
            'Active Mean': [],
            'Fwd Pkt Len Min': [],
            'FIN Flag Cnt': [],
            'Active Max': [],
            'Flow IAT Mean': [],
            'Down/Up Ratio': [],
            'Flow Byts/s': [],
            'Fwd Pkt Len Mean': [],
            'Fwd Seg Size Avg': [],
            'Flow IAT Std': [],
            'Fwd IAT Std': [],
            'Flow IAT Min': [],
            'Fwd IAT Mean': [],
            'Flow IAT Max': [],
            'Fwd IAT Max': [],
            'Fwd IAT Min': [],
            'Bwd IAT Min': [],
            'Idle Min': [],
            'Tot Fwd Pkts': [],
            'Idle Mean': [],
            'Fwd Act Data Pkts': [],
            'TotLen Fwd Pkts': [],
            'Idle Max': [],
            'Fwd Header Len': [],
            'TotLen Bwd Pkts': [],
            'Tot Bwd Pkts': [],
            'Bwd Header Len': [],
            'Active Std': [],
            'SYN Flag Cnt': [],
        }
        print("prcessing")
        for flow_key, data in flow_data.items():
            timestamps = data['timestamps']
            lengths = data['lengths']
            
            # Calculate features
            flow_duration = max(timestamps) - min(timestamps)
            flow_packets = [packet for packet in packets if IP in packet and packet[IP].src == flow_key[0] and packet[IP].dst == flow_key[1]]
            tot_fwd_pkts = len([packet for packet in flow_packets if packet[IP].src == flow_key[0]])
            tot_bwd_pkts = len([packet for packet in flow_packets if packet[IP].dst == flow_key[1]])
            tot_len_fwd_pkts = sum(len(packet) for packet in flow_packets if packet[IP].src == flow_key[0])
            tot_len_bwd_pkts = sum(len(packet) for packet in flow_packets if packet[IP].src == flow_key[1])
            fwd_pkt_len_min = min(len(packet) for packet in flow_packets if packet[IP].src == flow_key[0])
            fwd_pkt_len_mean = statistics.mean(len(packet) for packet in flow_packets if packet[IP].src == flow_key[0])
            fwd_seg_size_avg = sum(len(packet.payload) for packet in flow_packets if IP in packet and TCP in packet) / len([packet.payload for packet in flow_packets if IP in packet and TCP in packet]) if flow_packets and len([packet.payload for packet in flow_packets if IP in packet and TCP in packet]) != 0 else 0

            flow_byts_s = tot_len_fwd_pkts / flow_duration if flow_duration != 0 else 0
            flow_pkts_s = (tot_fwd_pkts + tot_bwd_pkts) / flow_duration if flow_duration != 0 else 0
            flow_iat = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
            flow_iat_mean = statistics.mean(flow_iat) if len(flow_iat) > 0 else 0  # Add check for at least one data point
            flow_iat_std = statistics.stdev(flow_iat) if len(flow_iat) > 1 else 0  # Add check for minimum two data points
            flow_iat_max = max(flow_iat) if flow_iat else 0
            flow_iat_min = min(flow_iat) if flow_iat else 0
            fwd_iat_mean = statistics.mean(flow_iat) if len(flow_iat) > 0 else 0  # Add check for at least one data point
            fwd_iat_std = statistics.stdev(flow_iat) if len(flow_iat) > 1 else 0  # Add check for minimum two data points
            fwd_iat_max = max(flow_iat) if flow_iat else 0
            bwd_iat_min = min(flow_iat) if flow_iat else 0
            idle_min = timestamps[-1] - timestamps[0]
            init_bwd_win_byts = flow_packets[0].window if TCP in flow_packets[0] else 0
            active_min = flow_duration - (timestamps[-1] - timestamps[0])
            active_mean = timestamps[-1] - timestamps[0] - active_min
            fin_flag_cnt = sum([1 for packet in flow_packets if IP in packet and TCP in packet and packet[TCP].flags & 0x01])
            active_max = max(flow_iat) if flow_iat else 0
            down_up_ratio = 1 if tot_len_bwd_pkts == 0 else tot_len_fwd_pkts / tot_len_bwd_pkts
            fwd_pkts_s = tot_fwd_pkts / flow_duration if flow_duration != 0 else 0
            bwd_pkts_s = tot_bwd_pkts / flow_duration if flow_duration != 0 else 0
            fwd_header_len = sum(len(packet) for packet in flow_packets if IP in packet and TCP in packet)
            bwd_header_len = sum(len(packet) for packet in flow_packets if IP in packet and TCP in packet)
            active_std = statistics.stdev(flow_iat) if len(flow_iat) > 1 else 0
            fwd_act_data_pkts = len([1 for packet in flow_packets if IP in packet and TCP in packet and packet[TCP].flags & 0x18])
            syn_flag_cnt = data['syn_count']
            
            # Additional check for flow_iat_min
            if flow_iat:
                fwd_iat_min = min(flow_iat)
            else:
                fwd_iat_min = 0
            
            # Append calculated features to lists
            flow_features['Fwd Pkts/s'].append(float(fwd_pkts_s))
            flow_features['Flow Pkts/s'].append(float(flow_pkts_s))
            flow_features['Bwd Pkts/s'].append(float(bwd_pkts_s))
            flow_features['Init Bwd Win Byts'].append(float(init_bwd_win_byts))
            flow_features['Active Min'].append(float(active_min))
            flow_features['Active Mean'].append(float(active_mean))
            flow_features['Fwd Pkt Len Min'].append(float(fwd_pkt_len_min))
            flow_features['FIN Flag Cnt'].append(float(fin_flag_cnt))
            flow_features['Active Max'].append(float(active_max))
            flow_features['Flow IAT Mean'].append(float(flow_iat_mean))
            flow_features['Down/Up Ratio'].append(float(down_up_ratio))
            flow_features['Flow Byts/s'].append(float(flow_byts_s))
            flow_features['Fwd Pkt Len Mean'].append(float(fwd_pkt_len_mean))
            flow_features['Fwd Seg Size Avg'].append(float(fwd_seg_size_avg))
            flow_features['Flow IAT Std'].append(float(flow_iat_std))
            flow_features['Fwd IAT Std'].append(float(fwd_iat_std))
            flow_features['Flow IAT Min'].append(float(flow_iat_min))
            flow_features['Fwd IAT Mean'].append(float(fwd_iat_mean))
            flow_features['Flow IAT Max'].append(float(flow_iat_max))
            flow_features['Fwd IAT Max'].append(float(fwd_iat_max))
            flow_features['Fwd IAT Min'].append(float(fwd_iat_min))
            flow_features['Bwd IAT Min'].append(float(bwd_iat_min))
            flow_features['Idle Min'].append(float(idle_min))
            flow_features['Tot Fwd Pkts'].append(float(tot_fwd_pkts))
            flow_features['Idle Mean'].append(float(statistics.mean([idle_min])))
            flow_features['Fwd Act Data Pkts'].append(float(fwd_act_data_pkts))
            flow_features['TotLen Fwd Pkts'].append(float(tot_len_fwd_pkts))
            flow_features['Idle Max'].append(float(idle_min))  # Since there's only one value, it's also the maximum
            flow_features['Fwd Header Len'].append(float(fwd_header_len))
            flow_features['TotLen Bwd Pkts'].append(float(tot_len_bwd_pkts))
            flow_features['Tot Bwd Pkts'].append(float(tot_bwd_pkts))
            flow_features['Bwd Header Len'].append(float(bwd_header_len))
            flow_features['Active Std'].append(float(active_std))
            flow_features['SYN Flag Cnt'].append(float(syn_flag_cnt))

            # print(flow_features)
        return flow_features
    def _make_predictions(self, flow_features):
        # Load the model
            model = keras.models.load_model(self.model_path)
    
    # Convert flow_features to DataFrame
            df = pd.DataFrame(flow_features)
            
            # Normalize the features
            scaler = StandardScaler()
            X_normalized = scaler.fit_transform(df)
            # df = df[df['Fwd Pkts/s'] != 0] # drop those rows in which fwd pkts is zero 
            # Make predictions
            predictions = model.predict(X_normalized)
            print(predictions)

            # Convert probabilities to classes based on threshold (0.5 for binary classification)
            # Assuming binary classification
            y_pred = np.where(predictions > 0.5, 1, 0)

            # Add the predicted labels as a new column to the DataFrame
            df['Predicted_Label'] = y_pred

            # Save the data with predicted labels to a new CSV file
            df.to_csv('data_with_predictions.csv', index=False)

            return predictions
    def _append_predictions_to_file(self, predictions):
        output_file = "x.txt"
        print("Appending predictions to file...")
        try:
            with open(output_file, 'a') as f:
                for prediction in predictions:
                    f.write(f"{prediction}\n")
            print(f"Predictions appended to {output_file}")
        except Exception as e:
            print(f"Error occurred while appending predictions to {output_file}: {e}")

        # print(f"Predictions appended to {output_file}")
    def _write_to_csv(self, flow_features):
        df = pd.DataFrame(flow_features)
        df.to_csv(self.csv_output, index=False)
        print(f"Conversion completed. CSV file saved as {self.csv_output}")

if __name__ == "__main__":
    converter = PcapToCsvConverter("output.pcap", "outputnew678912.csv", "botnet_detection_model.h5")
    converter.convert()