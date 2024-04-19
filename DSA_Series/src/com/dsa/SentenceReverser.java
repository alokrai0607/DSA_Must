package com.dsa;

public class SentenceReverser {
	public static String reverseSentence(String sentence) {
		
		String[] words = sentence.split(" ");
		StringBuilder sb = new StringBuilder();

		for (int i = words.length - 1; i >= 0; i--) {
			sb.append(words[i]);
			if (i > 0) {
				sb.append(" ");
			}
		}
		return sb.toString();
	}
	public static void main(String[] args) {
		String sentence = "Hello bro where are you going please tell me ";
		String res = reverseSentence(sentence);
		System.out.println(res);
	}

}
