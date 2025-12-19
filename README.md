# Bike Delivery Time Prediction 🚴‍♂️

A beginner-friendly PyTorch project that compares **Linear Regression** vs **Neural Networks** for predicting bike delivery times based on distance.

## 📋 Overview

This project demonstrates the fundamentals of machine learning by training two models to predict delivery times:
- A simple **Linear Model** (straight-line regression)
- A **Neural Network** with hidden layers

Both models learn from the same small dataset of 4 delivery examples and are compared side-by-side.

## 🎯 Learning Objectives

- Understand the difference between linear and neural network models
- Learn basic PyTorch concepts: tensors, loss functions, optimizers
- Visualize model training and predictions
- Compare model complexity vs performance

## 🚀 Quick Start

### Prerequisites

```bash
pip install torch matplotlib numpy
```

### Running the Code

```bash
python bike_delivery_prediction.py
```

## 📊 Dataset

The training data consists of 4 bike deliveries:

| Distance (miles) | Delivery Time (minutes) |
|------------------|-------------------------|
| 1.0              | 6.96                    |
| 2.0              | 12.11                   |
| 3.0              | 16.77                   |
| 4.0              | 22.21                   |

The models learn to predict delivery time for **7.0 miles** (outside the training range).

## 🧠 Models

### Linear Model
```
Architecture: 1 → 1 (input → output)
Parameters: 2 (weight and bias)
Equation: time = weight × distance + bias
```

### Neural Network
```
Architecture: 1 → 8 → 4 → 1
Parameters: 45 total
Layers:
  - Input: 1 neuron (distance)
  - Hidden 1: 8 neurons + ReLU
  - Hidden 2: 4 neurons + ReLU
  - Output: 1 neuron (time)
```

## 📈 Visualizations

The script generates three plots:

1. **Model Predictions**: Shows how each model fits the data
2. **Training Loss**: Tracks learning progress over 1,000 epochs
3. **Prediction Errors**: Compares residuals on training data

## 🔍 Key Findings

For this dataset, **both models perform similarly** because the relationship between distance and time is approximately linear. The linear model is preferred for its:
- Simplicity and interpretability
- Faster training time
- Lower risk of overfitting

The neural network would shine with more complex, non-linear relationships.

## 💡 When to Use Each Model

### Linear Model ✓
- Simple, proportional relationships
- Easy interpretation needed
- Limited training data
- Fast predictions required

### Neural Network ✓
- Complex patterns with curves
- Multiple interacting features
- Non-linear relationships
- Abundant training data

## 🛠️ Customization

Try modifying these parameters:

```python
# Training configuration
num_epochs = 1000        # Number of training iterations
lr = 0.01               # Learning rate

# Neural network architecture
nn.Linear(1, 8),        # Change hidden layer sizes
nn.Linear(8, 4),        

# Add more training data
distance = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
time = torch.tensor([[...]])  # Add corresponding times
```

## 📚 Code Structure

```
├── Data Preparation      # Load distance and time data
├── Linear Model          # Simple regression training
├── Neural Network        # Deep learning training
├── Predictions           # Test both models on 7 miles
├── Model Analysis        # Compare parameters and equations
└── Visualizations        # Generate comparison plots
```

## 🔧 Technical Details

- **Framework**: PyTorch 2.x
- **Loss Function**: Mean Squared Error (MSE)
- **Optimizer**: Stochastic Gradient Descent (SGD)
- **Training**: 1,000 epochs for both models
- **Activation**: ReLU (Rectified Linear Unit)

## 📖 Educational Notes

This project is ideal for:
- Machine learning beginners
- PyTorch newcomers
- Understanding model selection
- Comparing simple vs complex models

## 🤝 Contributing

Feel free to:
- Add more sophisticated models
- Experiment with different architectures
- Include real-world delivery data
- Add cross-validation or train/test splits

## 📄 License

Open source - use for learning and experimentation!

## 🎓 Next Steps

After mastering this project, try:
1. Adding more features (weather, traffic, time of day)
2. Using real delivery data
3. Implementing different optimizers (Adam, RMSprop)
4. Adding regularization to prevent overfitting
5. Creating a web interface for predictions

---

**Happy Learning! 🚀**
