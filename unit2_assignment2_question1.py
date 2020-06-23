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
      "enter the value  of a5\n",
      "enter the value  of b7\n",
      "enter the value  of c4\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "def maximum(a, b, c): \n",
    "  \n",
    "    if (a >= b) and (a >= c): \n",
    "        largest = a \n",
    "  \n",
    "    elif (b >= a) and (b >= c): \n",
    "        largest = b \n",
    "    else: \n",
    "        largest = c \n",
    "          \n",
    "    return largest \n",
    "    \n",
    "a =input(\"enter the value  of a\") \n",
    "b = input(\"enter the value  of b\")\n",
    "c = input(\"enter the value  of c\")\n",
    "print(maximum(a, b, c))"
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
