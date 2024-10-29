text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model")
inputs = tokenizer(text, return_tensors="pt")

from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")
with torch.no_grad():
    logits = model(**inputs).logits


from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")
with torch.no_grad():
    logits = model(**inputs).logits
    print(logits)