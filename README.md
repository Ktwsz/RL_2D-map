# Reinforcement Learning Model trained to reach right-down corner of a 2D Matrix starting from any position.

## Environment
10x10 matrix filled with zeroes. Agent's postion is marked by 1 at corresponding index. Agent gets +1 reward if he moves to the right or down, -1 if he's trying to go out of bounds and -2 if he's going left or up.

## Model
Implemented SARSA algorithm using TensorFlow, input is state of environment - 100 element vector(flattened matrix), output is 4 element vector [R<sub>left</sub>, R<sub>up</sub>, R<sub>right</sub>, R<sub>down</sub>] where R is predicted reward for going in a given direction

One hidden layer with 64 nodes, using ReLU for nonlinearity, TensorFlow's Adam optimizer.

## Dependencies required
TensorFlow, Pygame(for visual display of results)

## Usage
To train and export model to file model.pt run main.py 

To see results run showcase.py (you have to specify which model you want to use by changing models file load directory directly in script)

You can train the model either by always starting at (0, 0) or by starting at random position in order to sample more learning experiences. Interestingly, due to the simplicity of environment, high epoch number and exploration ratio model trained by always starting from (0, 0) can also reach the end from every position.
