# Huzi Chatbot

Welcome to the Huzi Chatbot! This project uses Streamlit for the UI and LangChain with the OpenAI API to create an interactive chatbot that answers questions about the Huzi restaurant based on provided data.

## Features

- Interactive chatbot interface built with Streamlit
- Answers questions based on restaurant data provided in a text file
- Uses LangChain and OpenAI API for generating responses

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:

   git clone 'https://github.com/yourusername/huzi-chatbot.git'
   cd huzi-chatbot

2. Create a virtual environment and activate it:
  
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:

   pip install streamlit langchain openai python-dotenv

4. Create a '.env' file in the project directory and add your OpenAI API key:
   
   OPENAI_API_KEY=your_openai_api_key

5. Prepare your restaurant data:

   Create a 'data.txt' file with the information about your restaurant. An example structure is provided below.

Usage:

1. Run the streamlit app:

   streamlit run StreamlitAPP.py

2. Open the URL provided by Streamlit (usually 'http://localhost:8501') in your web browser.

3. Ask questions about the Huzi restaurant, and the chatbot will respond based on the data provided in 'data.txt'.

Example 'data.txt':

# Huzi Restaurant Information

## General Information
Welcome to Huzi! We are dedicated to serving our customers with the best quality food and excellent service.

## Timings
- Monday to Thursday: 10:00 AM - 11:00 PM
- Friday: 10:00 AM - 12:00 AM
- Saturday: 9:00 AM - 12:00 AM
- Sunday: 9:00 AM - 10:00 PM

## Special Foods
- Original Recipe Chicken: Our signature fried chicken with 11 herbs and spices.
- Hot & Spicy Chicken: A spicy twist on our classic recipe.
- Zinger Burger: A crispy, spicy chicken fillet sandwich.
- Popcorn Chicken: Bite-sized, boneless pieces of crispy chicken.

## Deals
- Family Bucket: 8 pieces of Original Recipe Chicken, 4 biscuits, 2 large sides - $20.99
- Chicken Combo: 2 pieces of chicken, 1 side, 1 biscuit, 1 drink - $8.99
- Zinger Meal: Zinger Burger, 1 side, 1 drink - $7.99

## Midnight Deals
- Midnight Chicken Bucket: 6 pieces of Original Recipe Chicken, 2 sides, 2 biscuits - $15.99
- Late Night Snack: 10 pieces of Hot Wings, 1 large fries - $12.99

## Contact Information
- Address: 123 Huzi Lane, Food City, FC 12345
- Phone: (123) 456-7890
- Email: contact@huzirestaurant.com

## Frequently Asked Questions
### What are your opening hours?
Our opening hours are Monday to Thursday from 10:00 AM to 11:00 PM, Friday from 10:00 AM to 12:00 AM, Saturday from 9:00 AM to 12:00 AM, and Sunday from 9:00 AM to 10:00 PM.

### Do you offer any vegetarian options?
Yes, we offer a variety of vegetarian options including our Veggie Burger, Corn on the Cob, and various salads.

### What are your current deals?
We have several deals including the Family Bucket for $20.99, Chicken Combo for $8.99, and Zinger Meal for $7.99.

### Do you have any late-night deals?
Yes, we offer midnight deals such as the Midnight Chicken Bucket for $15.99 and the Late Night Snack for $12.99.

### How can I contact you?
You can reach us at (123) 456-7890 or email us at contact@huzirestaurant.com. Our address is 123 Huzi Lane, Food City, FC 12345.

### Do you have delivery services?
Yes, we offer delivery services through various platforms like Uber Eats, DoorDash, and our own Huzi delivery service.

### What payment methods do you accept?
We accept cash, credit cards, debit cards, and mobile payments like Apple Pay and Google Pay.

### Are there any special promotions for birthdays?
Yes, we offer a special birthday deal where you can get a free dessert with any meal purchase on your birthday. Just show a valid ID to redeem this offer.

### Do you offer catering services?
Yes, we provide catering services for events and parties. Please contact us at (123) 456-7890 for more details and to make arrangements.

### Is there a loyalty program?
Yes, we have a loyalty program called Huzi Rewards. Sign up on our website or app to earn points with every purchase and redeem them for discounts and free items.

### Are there any gluten-free options?
Yes, we offer several gluten-free options including our Grilled Chicken, Green Beans, and Coleslaw.


   
   
