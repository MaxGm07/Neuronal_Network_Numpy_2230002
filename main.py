from src.Numpy_Neuronal_Network import train_neural_network

def main():

    params = train_neural_network() # Llamar a la función de entrenamiento desde red_2.py
    print(params) 
        
if __name__ == "__main__":
    main()