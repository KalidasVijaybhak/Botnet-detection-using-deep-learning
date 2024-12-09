# Botnet detection using deep learning techniques (CNN-LSTM Hybrid Model) 


https://github.com/user-attachments/assets/38f02e73-9985-482f-ae53-b62370f4dbf9


# Deep Learning Approach for Botnet Detection from Raw Network Traffic Data

![Botnet Detection](link_to_banner_image)

## Overview
This project aims to develop an adaptive botnet detection system using deep learning techniques to overcome the limitations of signature-based and rule-based methods. The system is designed to analyze raw network traffic data and identify patterns and anomalies indicative of botnet activity.

## Table of Contents
1. [Introduction](#introduction)
2. [What is a Botnet?](#what-is-a-botnet)
3. [Relevance of Botnet Detection](#relevance-of-botnet-detection)
4. [Problem Statement](#problem-statement)
5. [Aim](#aim)
6. [Dataset](#dataset)
7. [Model Architecture](#model-architecture)
8. [User Interface](#user-interface)
9. [Timeline](#timeline)
10. [Conclusion](#conclusion)
11. [Contributors](#contributors)
12. [License](#license)
13. [Acknowledgments](#acknowledgments)

## Introduction
The modern world is heavily reliant on digital technology, making cybersecurity a critical concern. Cyberattacks, such as malware, phishing, ransomware, and DDoS attacks, disrupt operations, steal information, and cause financial harm. Deep learning algorithms can analyze vast amounts of data, identifying patterns and anomalies that may be indicative of cyber threats, even those that evolve and adapt over time.

## What is a Botnet?
A botnet is a network of compromised computers, known as "bots," controlled by a central server, often without the knowledge of the device owners. These bots can be used to perform various malicious activities, including:

- **Spam Generation**: Sending large volumes of unsolicited emails.
- **DDoS Attacks**: Overwhelming a target server with traffic to make it unavailable.
- **Infecting Systems**: Spreading malware to other devices.
- **Phishing**: Tricking users into revealing sensitive information.

![How a Botnet Works](link_to_botnet_image)

## Relevance of Botnet Detection
Botnets pose significant threats to cybersecurity, leading to financial losses, legal issues, and damage to reputation. Effective botnet detection is crucial for:

- **Protecting Networks**: Preventing unauthorized access and data breaches.
- **Maintaining Service Availability**: Ensuring that services remain accessible and functional.
- **Safeguarding Sensitive Information**: Protecting user data and intellectual property.

## Problem Statement
Develop an adaptive botnet detection system using deep learning techniques to overcome the limitations of signature-based and rule-based methods, ensuring effective detection of evolving tactics in network traffic.

## Solution
- Utilize deep learning techniques, which have demonstrated remarkable success in various fields, including computer vision and natural language processing intrusion detection systems.
- Use raw network traffic data as input, allowing the system to learn patterns and behaviors associated with botnet activity.
- Train deep neural networks to automatically detect botnet behavior without relying on predefined signatures or rules.

## Aim
- Develop a live capturing module using Wireshark to capture live network traffic for analysis.
- Develop a deep learning-based botnet detection system for dynamic adaptation to evolving tactics, overcoming limitations of static methods.
- Design different DL models and test for best performance.
- Design a simple and user-friendly User-Interface (UI) for easy use.

## Dataset
The CTU-13 dataset is a collection of network traffic data commonly used for botnet detection systems (IDS). It contains network traffic captures from a diverse range of botnet and normal activities, providing a valuable resource for cybersecurity research and development.

### Feature Extraction
- **Correlation**: Denotes the statistical association or relationship between two or more variables.
- We have tried different feature extraction methods like information gain.
- By Information gain, the accuracy obtained from the CNN-LSTM model was about 96.32%, which was lower compared to features selected from Correlation.

### Selected Features
- SYN Flag Cnt
- Active Min, Active Max
- Fwd Pkts/s, Flow Pkts/s, Bwd Pkts/s
- Init Bwd Win Byts
- Active Mean
- Fwd Pkt Len Min
- Bwd IAT Tot
- FIN Flag Cnt
- Bwd Pkt Len Std
- Pkt Size Avg, Pkt Len Std
- Flow IAT Mean
- Pkt Len Mean
- Bwd PSH Flags
- Bwd Pkt Len Max
- Pkt Len Max

## Model Architecture
### Models
- **CNN-LSTM**: Combines the strengths of both Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) networks.
- **Transformers**: Utilizes an attention mechanism to capture long-range dependencies in the data.
- **BiLSTM**: Processes the sequence in both directions, combining information from past and future states.

### Observations
| Model       | Accuracy (%) | Precision (%) | Recall (%) | F1-score (%) |
|-------------|--------------|---------------|------------|--------------|
| CNN-LSTM    | 97.87        | 97.15         | 97.83      | 97.49        |
| Bi-LSTM     | 97.09        | 96.49         | 96.64      | 96.56        |
| TRANSFORMER | 94.41        | 93.08         | 93.70      | 93.39        |

## User Interface
- Built using Python Tkinter and CustomTkinter.
- Utilizes multi-threading to run multiple processes in the background.
- Features:
  - Basic analytics like Network name, upload speed, download speed, etc.
  - Live network capture and detection of botnet.
  - Live network capture and converting to PCAP with the option to choose required features.
- The UI uses the CNN-LSTM model due to its higher accuracy on unseen network data.

## Timeline
![Project Timeline](link_to_timeline_image)

## Conclusion
Conventional botnet detection tools, which often rely on signature-based or rule-based approaches, can be effective in certain scenarios but also have limitations when it comes to detecting modern and sophisticated botnets. By training on diverse datasets, the models attain a deep understanding of normal network behavior, allowing them to identify deviations indicative of botnet activity. From analyzing different models, the best model used in the application is the CNN-LSTM hybrid model.

## Contributors
- **Guide**: Dr. Soniya B HOD, CS Dept.
- **Team Members**:
  - Kalidas V B (338)
  - Muhammed Nahal M (348)
  - Bristo Babu (364)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to the Czech Technical University (CTU) in Prague for providing the CTU-13 dataset.
- Thanks to the open-source community for tools like Wireshark, Scapy, and Python libraries that made this project possible.
