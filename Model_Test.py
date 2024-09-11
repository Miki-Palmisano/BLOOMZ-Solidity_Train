from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("/content/drive/MyDrive/Model-Training/Model-GPT3/saved_tokenizer")
model = AutoModelForCausalLM.from_pretrained("/content/drive/MyDrive/Model-Training/Model-GPT3/saved_model")

# Define a function to generate text without including the prompt
def generate_text(prompt):
    max_length=512
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    # Get the ID of the end-of-sequence token
    eos_token_id = tokenizer.eos_token_id
    output = model.generate(inputs, max_length=max_length, num_return_sequences=1, eos_token_id=eos_token_id)
    # Decode the output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    # Remove the prompt from the generated text
    generated_text = generated_text.replace(prompt, '', 1)
    return generated_text

# Prompt for generating text
prompt = "Make empty library."

# Generate text based on the prompt
generated_text = generate_text(prompt)
print("Generated text:\n", generated_text)
