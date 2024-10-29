from huggingface_hub import notebook_login

notebook_login()

#loading IMDB dataset
from datasets import load_dataset

imdb = load_dataset("imdb")

