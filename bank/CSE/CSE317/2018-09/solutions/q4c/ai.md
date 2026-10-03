---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A deep convolutional network learns the features itself: stacked convolution + ReLU + pooling layers turn raw pixels into a hierarchy of features (edges, textures, parts, objects); fully connected layers and a softmax give class probabilities; trained end-to-end by backpropagation and SGD on large labeled data sets (e.g. ImageNet)."
sources: ["AIMA 4e sec. 21.3 (convolutional networks) and 27.4 (image classification)"]
---
**Concept.** In classical image classification, an engineer designed the features (edges, SIFT, HOG) and a separate classifier used them. **Deep learning learns the features and the classifier together**, directly from raw pixels, with a deep neural network trained end-to-end. The standard architecture is the **convolutional neural network (CNN)**.

- **Convolution layers:** small learned filters (kernels, e.g. $3\times3$) slide over the image. They share weights across positions, so they detect the same pattern anywhere (translation invariance), with far fewer parameters than a fully connected layer.
- **Non-linearity** (ReLU) after each convolution.
- **Pooling** (max or average) down-samples the feature maps, adding robustness to small shifts and enlarging the receptive field.
- **Hierarchy:** early layers learn edges and colours, middle layers textures and parts, deep layers whole objects (faces, wheels).
- **Fully connected layers + softmax** at the end output a probability for each class.
- **Training:** minimize the cross-entropy loss on a large labeled data set (e.g. ImageNet, 1.2M images in 1000 classes) by backpropagation and stochastic gradient descent, with data augmentation, dropout and batch normalization against overfitting. Transfer learning (fine-tuning a pre-trained network) works for small data sets.
