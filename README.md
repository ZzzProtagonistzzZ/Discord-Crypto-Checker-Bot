# Crypto Price Discord Bot  

This is a **Discord bot** that allows users to check the real-time price of cryptocurrencies in different currencies (USD, EUR, and GBP) using the **CoinGecko API**.  

## Features  
✅ Check crypto prices in **USD, EUR, and GBP**  
✅ Get results in an **embedded message** for better readability  
✅ Uses **slash commands** for easy interaction  
✅ Built with **Discord.py** and **CoinGecko API**  

## Commands  
🔹 `/check_price_usd <coin>` – Get the price of a cryptocurrency in USD  
🔹 `/check_price_eur <coin>` – Get the price of a cryptocurrency in EUR  
🔹 `/check_price_gbp <coin>` – Get the price of a cryptocurrency in GBP  

## How It Works  
1. The bot listens for commands like `/check_price_usd bitcoin`.  
2. It fetches the latest price data from the **CoinGecko API**.  
3. The bot responds with an **embedded message** showing the price.  

## Setup  
1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/crypto-price-bot.git
   cd crypto-price-bot
   ```  
2. Install dependencies:  
   ```sh
   pip install discord requests
   ```  
3. Replace `"YOUR_BOT_TOKEN"` in the script with your **Discord bot token**.  
4. Run the bot:  
   ```sh
   python bot.py
   ```  

## Future Improvements  
🔹 Add more currencies and crypto options  
🔹 Implement a **dropdown menu & button UI** for easier selection  
🔹 Improve error handling for invalid coin names  

