import kagglehub

path = kagglehub.dataset_download(
    "samuelcortinhas/cats-and-dogs-image-classification"
)

print("Path to dataset files:", path)
