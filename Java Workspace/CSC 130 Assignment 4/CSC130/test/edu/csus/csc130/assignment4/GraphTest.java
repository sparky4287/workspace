//package edu.csus.csc130.assignment4;
package CSC130.test.edu.csus.csc130.assignment4;

import org.junit.Assert;

import org.junit.Test;

//remove below after assignment done
import CSC130.src.edu.csus.csc130.assignment4.Graph;

public class GraphTest {

	@Test
	public void testHasEdge1() {
		Graph graph = new Graph("tinyG.txt");
		Assert.assertTrue(Graph.hasEdge(graph, 0, 2));
	}
	
	@Test
	public void testHasEdge2() {
		Graph graph = new Graph("tinyG.txt");
		Assert.assertTrue(Graph.hasEdge(graph, 4, 3));
	}	
	
	@Test
	public void testHasEdge3() {
		Graph graph = new Graph("tinyG.txt");
		Assert.assertFalse(Graph.hasEdge(graph, 11, 10));
	}
	
	@Test
	public void testHasEdge4() {
		Graph graph = new Graph("tinyG.txt");
		Assert.assertFalse(Graph.hasEdge(graph, 20, 10));
	}	
	
	@Test
	public void testNumberOfParallelEdges1() {
		Graph graph = new Graph("tinyG.txt");
		Assert.assertEquals(0, Graph.numberOfParallelEdges(graph));
	}
	
	@Test
	public void testNumberOfParallelEdges2() {
		Graph graph = new Graph("tinyG_2ParallelEdges.txt");
		Assert.assertEquals(2, Graph.numberOfParallelEdges(graph));
	}	
	
	@Test
	public void testNumberOfParallelEdges3() {
		Graph graph = new Graph("tinyG_5ParallelEdges.txt");
		System.out.println(graph.toString());
		Assert.assertEquals(5, Graph.numberOfParallelEdges(graph));
	}	
	
	@Test
	public void testNumberOfParallelEdges4() {
		Graph graph = new Graph("tinyG_2ParallelEdges_1SelfLoop.txt");
		Assert.assertEquals(2, Graph.numberOfParallelEdges(graph));
	}	

}
