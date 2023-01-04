# Tensorflow: Identify Traffic Sign

## Config GPU tensorflow on M1 Pro

```
conda install -c apple tensorflow-deps
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal
```

I have to use specific version of tensorflow module to make that work on my laptop `tensorflow-macos==2.9` and `tensorflow-metal==0.5.0`.


## Experiments

My first version got 90% accuracy, because I use only 1 Convolutional Layer which is core in CNN, that means I have less feature extracted from image. After tried different combinations of kernel sizes and other hyperparameters, I ended up with more convolutional layers and current configurations.

```bash
python traffic.py gtsrb
Metal device set to: Apple M1 Pro

systemMemory: 16.00 GB
maxCacheSize: 5.33 GB

2023-01-05 01:42:30.741387: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:305] Could not identify NUMA node of platform GPU ID 0, defaulting to 0. Your kernel may not have been built with NUMA support.
2023-01-05 01:42:30.741488: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:271] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 0 MB memory) -> physical PluggableDevice (device: 0, name: METAL, pci bus id: <undefined>)
2023-01-05 01:42:30.843661: W tensorflow/core/platform/profile_utils/cpu_utils.cc:128] Failed to get CPU frequency: 0 Hz
Epoch 1/10
2023-01-05 01:42:31.048340: I tensorflow/core/grappler/optimizers/custom_graph_optimizer_registry.cc:113] Plugin optimizer for device_type GPU is enabled.
500/500 [==============================] - 5s 10ms/step - loss: 2.1540 - accuracy: 0.5003
Epoch 2/10
500/500 [==============================] - 5s 10ms/step - loss: 0.5519 - accuracy: 0.8413
Epoch 3/10
500/500 [==============================] - 5s 9ms/step - loss: 0.2965 - accuracy: 0.9139
Epoch 4/10
500/500 [==============================] - 5s 9ms/step - loss: 0.2203 - accuracy: 0.9342
Epoch 5/10
500/500 [==============================] - 5s 10ms/step - loss: 0.1928 - accuracy: 0.9464
Epoch 6/10
500/500 [==============================] - 5s 10ms/step - loss: 0.1673 - accuracy: 0.9553
Epoch 7/10
500/500 [==============================] - 5s 10ms/step - loss: 0.1480 - accuracy: 0.9586
Epoch 8/10
500/500 [==============================] - 5s 10ms/step - loss: 0.1142 - accuracy: 0.9683
Epoch 9/10
500/500 [==============================] - 5s 10ms/step - loss: 0.1609 - accuracy: 0.9575
Epoch 10/10
500/500 [==============================] - 5s 10ms/step - loss: 0.1104 - accuracy: 0.9704
2023-01-05 01:43:19.724816: I tensorflow/core/grappler/optimizers/custom_graph_optimizer_registry.cc:113] Plugin optimizer for device_type GPU is enabled.
333/333 - 2s - loss: 0.0450 - accuracy: 0.9893 - 2s/epoch - 5ms/step
```

Teacher performence metric: loss: 0.1616 - accuracy: 0.9535. My 3% model higher than it.