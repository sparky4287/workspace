package com.mycompany.a1;

import java.util.Random;

abstract public class GameObject {

	protected Random rand = new Random();
	protected double locationX, locationY;
	protected int size, color;
	protected String center;
	
	public GameObject() {
		locationX = Double.valueOf(rand.nextInt(1024));
		locationY = Double.valueOf(rand.nextInt(768));
		center = "("+String.valueOf(locationX)+","+String.valueOf(locationY)+")";
	}
	
	public double getLocationX() {
		return locationX;
	}
	public double getLocationY() {
		return locationY;
	}
	public int getSize() {
		return size;
	}
	public int getColor() {
		return color;
	}
	public String getLocation() {
		return center;
	}
	
	public void setLocationX(double newLocationX) {
		if(newLocationX >= 0.0 && newLocationX <= 1024.0) {
			locationX = newLocationX;
		}
	}
	public void setLocationY(double newLocationY) {
		if(newLocationY >= 0.0 && newLocationY <= 768.0) {
			locationY = newLocationY;
		}
	}
	public void setSize(int newSize) {
		size = newSize;
	}
	public void setColor(int newColor) {
		color = newColor;
	}
	public void setLocation(double newX, double newY) {
		setLocationX(newX);
		setLocationY(newY);
		center = "("+String.valueOf(locationX)+","+String.valueOf(locationY)+")";
	}
}
