package com.mycompany.a1;

import java.util.Random;

import com.codename1.charts.util.ColorUtil;

public class Spaceship extends Rescuer {

	private Random ranInt = new Random();
	
	public Spaceship() {
		setSize(100);
	}
	
	public void setSize(int newSize) {
		if(newSize <= 1024 && newSize >= 50) {
			size = newSize;
		}
	}
	public void setColor(int newColor) {
		color = newColor;
	}
	
	public void move() {
		
	}
	
	public String toString() {
		return "Spaceship: loc=" + getLocation() +
			" color=[" + ColorUtil.red(color) + "," + 
				ColorUtil.green(color) + "," + 
				ColorUtil.blue(color) +
			"] size=" + getSize();
	}
}
