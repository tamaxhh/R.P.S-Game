{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4cf60a4a-5cd0-451d-87bf-de1457558686",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random as rn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 286,
   "id": "824d8e85-e609-4ecf-8b36-2354d6f58ed5",
   "metadata": {},
   "outputs": [],
   "source": [
    "P=0\n",
    "C=0\n",
    "D=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "id": "b27ed83c-6e59-4e43-8fd2-95a2ff08e3b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Player1 Chose : Stone\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Com Chose : Paper\n",
      "----Com: Win----\n",
      "No of Win by Player1: 4\n",
      "No of Win by Com: 1\n",
      "No of Draw: 2\n"
     ]
    }
   ],
   "source": [
    "player1 = input(\"Player1 Chose :\")\n",
    "Com = [\"Stone\",\"Paper\",\"Scissor\"]\n",
    "Com = rn.choice(Com)\n",
    "print(\"Com Chose :\",Com)\n",
    "\n",
    "\n",
    "if player1 == \"Stone\" or player1 == \"Paper\" or player1 == \"Scissor\":\n",
    "    if Com in [\"Stone\",\"Paper\",\"Scissor\"]:\n",
    "        if player1 == \"Stone\" and Com == \"Scissor\":\n",
    "            print(\"----Player1: Win----\")\n",
    "            P+=1\n",
    "        elif player1 == \"Stone\" and Com == \"Paper\":\n",
    "            print(\"----Com: Win----\")\n",
    "            C+=1\n",
    "        elif player1 == \"Paper\" and Com == \"Stone\":\n",
    "            print(\"----player1: Win----\")\n",
    "            P+=1\n",
    "        elif player1 == \"Paper\" and Com == \"Scissor\":\n",
    "            print(\"----Com: Win----\")\n",
    "            C+=1\n",
    "        elif player1 == \"Scissor\" and Com == \"stone\":\n",
    "            print(\"----Com: Win----\")\n",
    "            C+=1\n",
    "        elif player1 == \"Scissor\" and Com == \"Paper\":\n",
    "            print(\"----player1: Win----\")\n",
    "            P+=1\n",
    "        elif (player1 == \"Stone\" and Com == \"Stone\") or (player1 == \"Scissor\" and Com == \"Scissor\") or (player1 == \"Paper\" and Com == \"Paper\"):\n",
    "            print(\"----DRAW!!----\")  \n",
    "            D+=1\n",
    "else:\n",
    "    print(\"----Show Valid Moves!!!!----\")\n",
    "\n",
    "print(\"No of Win by Player1:\",P)\n",
    "print(\"No of Win by Com:\",C)\n",
    "print(\"No of Draw:\",D)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "686481d3-08e5-4562-aef9-dccd318dd228",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2c58e04-2755-407e-ae25-270025171c39",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2602997e-6755-4f76-8f35-716343dc4ca7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c179c09-6b7c-4c06-9c90-29adddd4d378",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
