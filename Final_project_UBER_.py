{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3753395e-dadf-47f1-b6cb-fcd730e2f7b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (5.4.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (1.8.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (5.4.0)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (24.0)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (5.27.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (17.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (8.4.1)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (6.4)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from streamlit) (4.0.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.22.0)\n",
      "Requirement already satisfied: narwhals>=1.1.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.3.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.1)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\rukma\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.0 -> 24.3\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43c3bb9a-db1e-4a77-afe6-430fe841abda",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import mysql.connector\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from datetime import datetime\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "def init_db():\n",
    "    return mysql.connector.connect(\n",
    "        host=\"localhost\",\n",
    "        user=\"root\",\n",
    "        password=\"123456\",\n",
    "        database=\"uber_data\"\n",
    "    )\n",
    "\n",
    "\n",
    "def extract_real_time_data(pickup, destination):    \n",
    "       data = {\n",
    "        \"fare_estimate\": np.random.uniform(100, 500), \n",
    "        \"wait_time\": np.random.randint(5, 15) \n",
    "    }\n",
    "    return data\n",
    "\n",
    "def predict_best_time(pickup, destination, time):\n",
    "    model = LinearRegression()\n",
    "    X = np.array([[1, 2, 3]])  # Example feature data\n",
    "    y = np.array([4])  # Example target data\n",
    "    model.fit(X, y)\n",
    "    predicted_fare = model.predict(np.array([[pickup, destination, time.hour]]))[0]\n",
    "    return round(predicted_fare, 2)\n",
    "\n",
    "st.title(\"Uber Ride Optimizer\")\n",
    "st.write(\"Get the best time to book an Uber ride based on predicted fare estimates.\")\n",
    "\n",
    "pickup_location = st.text_input(\"Enter Pickup Location\")\n",
    "destination = st.text_input(\"Enter Destination\")\n",
    "pickup_time = st.time_input(\"Enter Pickup Time\", datetime.now().time())\n",
    "\n",
    "if st.button(\"Get Fare Prediction\"):\n",
    "    if pickup_location and destination:\n",
    "        data = extract_real_time_data(pickup_location, destination)\n",
    "        st.write(f\"Estimated Fare: ${data['fare_estimate']}\")\n",
    "        st.write(f\"Estimated Wait Time: {data['wait_time']} minutes\")\n",
    "\n",
    "        # Predict best booking time (Placeholder model)\n",
    "        best_fare_prediction = predict_best_time(pickup_location, destination, pickup_time)\n",
    "        st.write(f\"Predicted Optimal Fare: ${best_fare_prediction}\")\n",
    "    else:\n",
    "        st.write(\"Please enter both pickup location and destination.\")\n",
    "\n",
    "def store_data(pickup, destination, fare, wait_time):\n",
    "    conn = init_db()\n",
    "    cursor = conn.cursor()\n",
    "    query = \"\"\"\n",
    "    INSERT INTO ride_data (pickup, destination, fare_estimate, wait_time, timestamp)\n",
    "    VALUES (%s, %s, %s, %s, %s)\n",
    "    \"\"\"\n",
    "    cursor.execute(query, (pickup, destination, fare, wait_time, datetime.now()))\n",
    "    conn.commit()\n",
    "    cursor.close()\n",
    "    conn.close()\n",
    "\n",
    "if st.button(\"Save Ride Data\"):\n",
    "    store_data(pickup_location, destination, data['fare_estimate'], data['wait_time'])\n",
    "    st.write(\"Data saved successfully.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}