from keras import models, layers, optimizers

def build_dqn(input_shape=(210, 160, 4), ACTIONS_SIZE=5, LEARNING_RATE=0.0001):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(ACTIONS_SIZE, activation='linear')
    ])

    optimizer = optimizers.Adam(learning_rate=LEARNING_RATE)
    
    model.compile(optimizer=optimizer,
                  loss='mse',  # Mean Squared Error for Q-learning
                  metrics=['accuracy'])

    return model