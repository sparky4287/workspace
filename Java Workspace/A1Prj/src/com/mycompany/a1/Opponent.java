package com.mycompany.a1;

import java.util.Random;
import java.lang.Math;

abstract public class Opponent extends GameObject implements IMove {
	
	private int direction, constant, speed;
	private Random rand = new Random(); 
	
	public Opponent() {
		setSize(20+rand.nextInt(50));
		direction = rand.nextInt(359);
		constant = 1;
		speed = 5 * constant;
	}
	
	public int getSpeed() {
		return speed;
	}
	public int getDirection() {
		return direction;
	}
	
	public void setSize(int newSize) {
		size = newSize;
	}
	public void setSpeed(int newSpeed) {
		speed = newSpeed;
	}
	public void setDirection(int newDirection) {
		direction = newDirection;
	}
	
	public void move() {
		setLocation(getLocationX()+(Math.cos(90-direction)*speed),
					getLocationY()+(Math.sin(90-direction)*speed));
	}
}
