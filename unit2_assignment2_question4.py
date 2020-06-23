{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any number : 354453\n",
      "The given number is PALINDROME\n"
     ]
    }
   ],
   "source": [
    "num = input('Enter any number : ')\n",
    "try:\n",
    "   val = int(num)\n",
    "   if num == str(num)[::-1]:\n",
    "      print('The given number is PALINDROME')\n",
    "   else:\n",
    "      print('The given number is NOT a palindrome')\n",
    "except ValueError:\n",
    "   print(\"That's not a valid number, Try Again !\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
