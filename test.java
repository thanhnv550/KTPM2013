/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package KTPM2013;

/**
 *
 * @author autorunx
 */

public class test {
    public static int gpt(int a, int b){
        if(a==0&&b==0){
            return 9999;
        }
        else if(a==0&&b!=0){
            return 0;
        }
        else return (int)b/a;
    }
    public static void test1(){
        if(gpt(0,0)==0)System.out.println("Dung test 1");
        else System.out.println("Sai test 1");
    }
    public static void test2(){
        if(gpt(1,1)==1)System.out.println("Dung test 2");
        else System.out.println("Sai test 2");
    }
    public static void test3(){
        if(gpt(0,1)==0)System.out.println("Dung test 3");
        else System.out.println("Sai test 3");
    }
     public static void testall(){
        test1();
        test2();
        test3();
    }
    public  static void main(String []args){
        testall();
    
    }
}
