package com.dsa;


import java.util.*;

public class WordFreqCounter {
    public static void main(String[] args) {
        String paragraph = "Alok Rai  is a good student , Alok is a good boy and he is masai alumanai ";

        //  Tokenization and normalization
        String[] words = paragraph.toLowerCase().split("\\s+");

        //  Counting
        Map<String, Integer> frequency = new HashMap<>();
        for (String word : words) {
            frequency.put(word, frequency.getOrDefault(word, 0) + 1);
        }

        //  Displaying Results
        for (Map.Entry<String, Integer> entry : frequency.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
