import re, json
from textblob import TextBlob

# Esempio di smart contract
smart_contract = """
contract Ownable {
 address public owner;
 event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
 /**
   * @dev The Ownable constructor sets the original `owner` of the contract to the sender
   * account.
   */
 constructor() public{
    owner = msg.sender;
 }
 /**
   * @dev Throws if called by any account other than the owner.
   */
 modifier onlyOwner() {
    require(msg.sender == owner);
    _;
 }
 /**
   * @dev Allows the current owner to transfer control of the contract to a newOwner.
   * @param newOwner The address to transfer ownership to.
   */
 function transferOwnership(address newOwner) onlyOwner public {
    require(newOwner != address(0));
    emit OwnershipTransferred(owner, newOwner);
    owner = newOwner; //Associa newOwner ad Owner
 }
}
"""

def convert_code(code):
    formatted_code = code.replace('\n', '\\n').replace('    ', '\\t')
    formatted_code = re.sub(r'//.*', '', formatted_code)
    return formatted_code

# Regex per trovare i commenti e il codice associato
comment_pattern = r"/\*\*.*?\*/"
code_pattern = r"(?<=\*/).*?(?=/\*\*|$)"

# Trova tutti i commenti e il codice associato
comments = re.findall(comment_pattern, smart_contract, re.DOTALL)
codes = re.findall(code_pattern, smart_contract, re.DOTALL)

# Pulisce i commenti e il codice per rimuovere i caratteri di formattazione
cleaned_comments = [re.sub(r"/\*\*|\*/|\@dev|\@param|\*|\n|   ", "", comment).strip() for comment in comments]
cleaned_codes = [code.strip() for code in codes]

cleaned_codes = [convert_code(code) for code in cleaned_codes]

file_path = "./smart_dataset.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Stampa i commenti e il codice separati
for comment, code in zip(cleaned_comments, cleaned_codes):
    new_element = {
    "input_text": comment,
    "output_code": code
    }
    data.append(new_element)

with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)
