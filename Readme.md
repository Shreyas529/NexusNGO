# Nexus NGO

NexusNGO is a platform designed to connect donors with NGOs, facilitating donations of items and funds. The platform also provides a user-friendly interface for NGOs to manage their profiles and interact with donors.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Testing](#testing)

---

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/NexusNGO.git
    cd NexusNGO
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the root directory.
    - Add your environment variables (e.g., `INFURA_API_KEY` for blockchain interaction).

4. **Run the application:**
    ```sh
    streamlit run NexusNGO/app.py
    ```

---

## Usage

### For Donors:
- Navigate through the sidebar to:
  - Donate items or funds.
  - Search for NGOs based on specific needs.
  - View top NGOs.

### For NGOs:
- Log in or register through the sidebar.
- Manage your profile, update information, and interact with donors.

---
## Project Structure

```
.gitignore
blockchain/
    blockchain.py
NexusNGO/
    app.py
    Firebase/
        authenticate.py
        cred.py
        db_interaction.py
    Image_Detection/
        image_to_text.py
        prompts.py
    Ngos/
        ngo_interface.py
        register_ngo.py
        update_ngo.py
    requirements.txt
    Users/
        search_ngos.py
        top_ngos.py
        user_interface.py
```

### Key Files and Directories

- **[`blockchain/blockchain.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fsathvik_rao%2FColossus%2FNexus_Public%2Fblockchain%2Fblockchain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22e01f52a6-1a46-49a1-b8fc-abdbb680daaf%22%5D "/home/sathvik_rao/Colossus/Nexus_Public/blockchain/blockchain.py")**: Contains functions for blockchain interactions, such as fetching transactions.
- **[`NexusNGO/app.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fsathvik_rao%2FColossus%2FNexus_Public%2FNexusNGO%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22e01f52a6-1a46-49a1-b8fc-abdbb680daaf%22%5D "/home/sathvik_rao/Colossus/Nexus_Public/NexusNGO/app.py")**: Main entry point for the Streamlit application.
- **[`NexusNGO/Firebase/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fsathvik_rao%2FColossus%2FNexus_Public%2FNexusNGO%2FFirebase%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22e01f52a6-1a46-49a1-b8fc-abdbb680daaf%22%5D "/home/sathvik_rao/Colossus/Nexus_Public/NexusNGO/Firebase/")**: Contains modules for Firebase authentication and database interactions.
- **[`NexusNGO/Image_Detection/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fsathvik_rao%2FColossus%2FNexus_Public%2FNexusNGO%2FImage_Detection%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22e01f52a6-1a46-49a1-b8fc-abdbb680daaf%22%5D "/home/sathvik_rao/Colossus/Nexus_Public/NexusNGO/Image_Detection/")**: Modules for image processing and text extraction.
- **[`NexusNGO/Ngos/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fsathvik_rao%2FColossus%2FNexus_Public%2FNexusNGO%2FNgos%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22e01f52a6-1a46-49a1-b8fc-abdbb680daaf%22%5D "/home/sathvik_rao/Colossus/Nexus_Public/NexusNGO/Ngos/")**: Modules for NGO-related functionalities, including registration and profile updates.
- **[`NexusNGO/Users/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fsathvik_rao%2FColossus%2FNexus_Public%2FNexusNGO%2FUsers%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22e01f52a6-1a46-49a1-b8fc-abdbb680daaf%22%5D "/home/sathvik_rao/Colossus/Nexus_Public/NexusNGO/Users/")**: Modules for user-related functionalities, including searching and displaying NGOs.

## Features

### Database Testing:
The Firebase database is initialized, and a testing class is created using Python's `unittest` library.

- **Add an NGO and verify the added data**: Check `ngo_name`, `category`, `needs`, and `email`.
- **Update NGO details**: Measures are taken to re-authenticate and retry in case of an expired session.
  - Update fields: `needs`, `description`, `phone`, and `category`.
  - Verify the updated data after retrieval.

### LLM (Image Detection) Testing:
- **Image Input**: For an image of a shirt, perform an `AssertTrue` to check if the output mentions "shirt."
- **Text Input**: When the donation contact includes "Shirt" and "Pant," verify that the response mentions these items.
- **Image Encoding**: Compare the encoding of an image using the application's function with Python's built-in encoding functions.

### Blockchain Testing:
- **Transaction Retrieval**: Use a public key to fetch transaction data from the last 3 minutes and verify the results.
- **Mock CSV Export**: Create a mock version of the pandas `to_csv` method to ensure it is called exactly once in the `get_transactions_last_3_minutes()` method with the correct arguments.

---

## Testing

### Database Testing:
- **Add and Verify NGO Data**: Ensure that NGO details are correctly added and retrieved.
- **Update NGO Details**: Verify that updates to NGO profiles are accurately reflected in the database.

### LLM (Image Detection) Testing:
- **Image and Text Input**: Validate the accuracy of image-to-text and text processing functionalities.
- **Image Encoding**: Ensure consistency in image encoding methods.

### Blockchain Testing:
- **Transaction Fetching**: Confirm that transaction data is correctly retrieved and exported.
- **Mock CSV Export**: Verify the correct usage of the `to_csv` method in blockchain interactions..
