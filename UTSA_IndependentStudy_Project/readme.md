# LearnableRegions: Text-Driven Image Editing via Learnable Regions

This repository contains the term project **LearnableRegions**, which implements a novel approach to text-driven image editing using Learnable Regions. The project was supervised by **Professor Paul Rad**.

## Paper
For a detailed understanding of the methodology and findings, please refer to the original paper:  
**[Text-Driven Image Editing via Learnable Regions](https://arxiv.org/pdf/2311.16432)**  
This paper introduces Learnable Regions, a new method for text-driven image editing that doesn't require user-provided masks or sketches. Instead, it uses a pre-trained text-to-image model and a region generation network to identify areas in the image that match the given text prompt. This approach enables localized and precise edits directly guided by the text.

The method can handle complex prompts, including descriptions with multiple objects or detailed sentences. It uses a combination of loss functions to ensure the edits are realistic, align well with the text, and maintain the original structure of the image. Experiments show that this method produces high-quality and accurate edits, performing as well as or better than existing approaches.

## Repository
The source code for this project is available here:  
[Learnable Regions - Project Page](https://yuanze-lin.me/LearnableRegions_page/)

## Objectives
1. **Learn the Approach**: Read the paper to understand the problem, methodology, and contributions of Learnable Regions.
2. **Understand the Code**: Study the implementation provided in the repository to comprehend how Learnable Regions are applied to text-driven image editing tasks.
3. **Reproduce Results**: Use the provided codebase to replicate the results presented in the paper.

## Prerequisites
Before starting, ensure the following:
- A working Python environment (Python 3.7 or later recommended).
- Required libraries and dependencies (refer to the instructions on the project page for installation details).
- Access to the datasets used in the study (check the paper for more details).

## Steps to Get Started
1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/<repository-link>.git
   cd LearnableRegions
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Familiarize yourself with the paper to understand the proposed methodology.
   - Follow the instructions provided in the repository to:
   - Prepare the dataset.
   - Train the model.
   - Evaluate the model performance and reproduce the results.
## Contribution Highlights

The Learnable Regions framework has several notable contributions:

A novel region-specific learning paradigm for image editing guided by textual descriptions.
State-of-the-art performance across various tasks, demonstrating both flexibility and precision in image editing.
Robust generalization to a variety of datasets and use cases.
## Acknowledgments

This project was completed under the supervision of Professor Paul Rad as part of the term project requirements.
