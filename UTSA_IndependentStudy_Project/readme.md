# FocusMAE: Gallbladder Cancer Detection from Ultrasound Videos with Focused Masked Autoencoders

This repository contains the term project **FocusMAE**, which implements a novel approach to gallbladder cancer detection from ultrasound videos using Focused Masked Autoencoders. The project was supervised by **Professor Paul Rad**.

## Paper
For a detailed understanding of the methodology and findings, please refer to the original paper:  
**[FocusMAE: Gallbladder Cancer Detection from Ultrasound Videos with Focused Masked Autoencoders](https://arxiv.org/abs/2403.08848)**
This paper highlights the growing interest in automated Gallbladder Cancer (GBC) detection and the limitations of current state-of-the-art methods using ultrasound (US) images, which struggle with generalization. The study shifts focus from image-based to video-based GBC detection, utilizing spatiotemporal representations for better results. It introduces FocusMAE, a novel Masked Autoencoder design that emphasizes high-information regions for refined cancer detection. The authors also present the largest US video dataset for GBC detection, achieving a new state-of-the-art accuracy of 96.4%, outperforming existing image-based and video-based methods. Additionally, the approach demonstrates broader applicability by improving accuracy on a public CT-based COVID-19 detection dataset.

## Repository
The source code for this project is available on GitHub:  
[https://github.com/sbasu276/FocusMAE](https://github.com/sbasu276/FocusMAE)

## Objectives
1. **Learn the Approach**: Familiarize yourself with the paper to understand the problem, methodology, and contributions.
2. **Understand the Code**: Study the implementation provided in the repository to understand how the Focused Masked Autoencoders are applied to the dataset.
3. **Reproduce Results**: Use the codebase to replicate the results presented in the paper.

## Prerequisites
Before you begin, ensure you have the following:
- A working Python environment (Python 3.7 or later recommended)
- Required libraries and dependencies as mentioned in the repository's `requirements.txt`
- Access to the dataset used in the study (refer to the paper for more details)

## Steps to Get Started
1. Clone the repository:
   ```bash
   git clone https://github.com/sbasu276/FocusMAE.git
   cd FocusMAE
   ```
2.Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Read the paper to understand the context and the methodology.
4. Follow the instructions in the repository to reproduce the results:
  ** Prepare the dataset
  ** Train the model
  ** Evaluate the performance

## Acknowledgments

This project was completed under the supervision of Professor Paul Rad as part of the term project requirements.


