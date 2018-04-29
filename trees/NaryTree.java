package com.learning;

import java.io.*;
import java.util.ArrayList;

class NaryNode {
  char data;
  ArrayList<NaryNode> children;

  public NaryNode(char data) {
    this.data = data;
    this.children = new ArrayList<NaryNode>(5);
//    for (int i = 0; i < 5; i++){
//      this.children.set(i, null);
//    }
  }


}

public class NaryTree{
  public NaryNode root;
  public NaryNode root1;

  public static final int no_of_childre= 5;

  public NaryTree(NaryNode root){
    this.root = root;
    this.root.children.add(new NaryNode('B'));
    this.root.children.add(new NaryNode('C'));
    this.root.children.add(new NaryNode('D'));
    this.root.children.get(0).children.add(new NaryNode('E'));
    this.root.children.get(0).children.add(new NaryNode('F'));
    this.root.children.get(2).children.add(new NaryNode('G'));
    this.root.children.get(2).children.add(new NaryNode('H'));
    this.root.children.get(2).children.add(new NaryNode('I'));
    this.root.children.get(2).children.add(new NaryNode('J'));

    this.root.children.get(0).children.get(1).children.add(new NaryNode('K'));

  }

  public void printTree(NaryNode root){
    if(null!=root){
      System.out.println(root.data);
      for(int i =0;i<root.children.size();++i){
        printTree(root.children.get(i));
      }
    }
  }

  public void serialise(NaryNode root,BufferedWriter writer){
    try {
    if(root== null){
      return;
    }
      writer.append(root.data);
      for(int i =0 ; i<root.children.size();++i){
        serialise(root.children.get(i),writer);
      }
      writer.append(")");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public boolean deserialise(NaryNode parentRoot, BufferedReader reader) {
    try {
      int c;
      if ((c = reader.read()) == -1 ||  (char)c == ')') {
        return true;
      }
      NaryNode root = new NaryNode((char)c);
      if(parentRoot == null) {
        this.root1 = root;
      } else if(parentRoot.children != null){
        parentRoot.children.add(root);
      }
      for (int i = 0; i <5; ++i) {
        if (deserialise(root, reader)) {
          break;
        }
      }
      return false;
    } catch (Exception e) {
      e.printStackTrace();
      return false;
    }
  }


  public static void main(String args[]){
    NaryNode root = new NaryNode('A');
    NaryTree tree = new NaryTree(root);
    tree.printTree(root);
    try {
      String fileName = "seriliase.txt";
      BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
      tree.serialise(root,writer);
      writer.close();

      BufferedReader reader = new BufferedReader(new FileReader(fileName));
      tree.root1 = null;
      tree.deserialise(tree.root1,reader);
      System.out.println("new tree");
      tree.printTree(tree.root1);
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }


  }

}
