package com.learning;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Stack;

public class Graph {
  private  int V;
  private LinkedList<Integer> adj[];

  //constructor which number of edges in the graph
  Graph(int v){
    this.V=v;
    this.adj = new LinkedList[v];
    for(int i=0 ; i<v; ++i){
      adj[i]=new LinkedList();
    }
  }

  void addEdge(Integer u, Integer v){
    this.adj[u].add(v);
  }

  void topologicalSortUtil(Integer v,boolean vistited[],Stack stack){

    vistited[v]= true;
    Integer i;

    Iterator<Integer> it = adj[v].iterator();

    while(it.hasNext()){
      i = it.next();
      if(!vistited[i]){
        topologicalSortUtil(i,vistited,stack);
      }
    }
    stack.push(new Integer(v));

  }

  void topologicalSort(Graph g){
    Stack stack = new Stack();

    boolean visited[] = new boolean[V];
    for(int i =0 ; i<V;++i){
      visited[i] = false;
    }

    for(int i =0 ; i< V; ++i){
      if(!visited[i]){
        topologicalSortUtil(i,visited,stack);
      }
    }

    while(stack.empty()==false){
      System.out.print(stack.pop() + "");
    }

  }

  public static void main(String args[]){
    Graph g = new Graph(6);
    g.addEdge(1,3);
    g.addEdge(2,3);
    g.addEdge(5,2);
    g.addEdge(5,0);
    g.addEdge(4,0);
    g.addEdge(4,1);

    g.topologicalSort(g);
  }

}
