{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11 is a prime number\n"
     ]
    }
   ],
   "source": [
    "num = 11\n",
    "  \n",
    "\n",
    "if num > 1: \n",
    "      \n",
    "   \n",
    "   for i in range(2, num): \n",
    "           \n",
    "       if (num % i) == 0: \n",
    "           print(num, \"is not a prime number\") \n",
    "           break\n",
    "   else: \n",
    "       print(num, \"is a prime number\") \n",
    "  \n",
    "else: \n",
    "   print(num, \"is not a prime number\") "
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
