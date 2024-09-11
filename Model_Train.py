from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments, AutoTokenizer, AutoModelForCausalLM
import json
import random

# Carico il tuo dataset JSON
with open('./Dataset.json', 'r') as file:
    dataset = json.load(file)

tokenizer = AutoTokenizer.from_pretrained("bigscience/bloomz-560m")
model = AutoModelForCausalLM.from_pretrained("bigscience/bloomz-560m")

# Preparo il dataset
tokenized_dataset = []

# Preparo il tokenized dataset
tokenized_dataset = []
for example in dataset:
    input_text = example["input_text"]
    output_code = example["output_code"]
    tokenized_example = tokenizer(input_text, output_code, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    tokenized_dataset.append(tokenized_example)

# Creo il DataLoader
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False,
)

# Configuro gli argomenti di training
training_args = TrainingArguments(
    output_dir="./finetuned",
    overwrite_output_dir=True,
    num_train_epochs=10,
    per_device_train_batch_size=1,
    save_steps=10000,
    save_total_limit=2,
    logging_steps=50,
    weight_decay=0.05
)

# Configuro il Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=tokenized_dataset,
)

# Avvio il fine-tuning
trainer.train()

# Salvo il modello fine-tuned
model.save_pretrained("./saved_model")

# Salvo il tokenizer
tokenizer.save_pretrained("./saved_tokenizer")
