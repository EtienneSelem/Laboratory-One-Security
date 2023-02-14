package chiffrement;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author Selem'n
 */

public class Chiffrement {

    /**
     * @param args the command line arguments
     */
    public static int [] permitation(int [] mot, int [] permut){
        int index=0;
        int[] tempo=new int[mot.length];
         for (int i =0; i < permut.length; i++) {
           index = permut[i];
          tempo[i] = mot[index];
         //K[i]=K[index];
          
          }
         mot=tempo;
         return mot;
    }
    public static List<int []> DivisionTabeau(int [] A){
        List<int []> list=new ArrayList<>();
        int taille = A.length;
       int longeurK1 = A.length/2;
      int longeurK2 = taille-longeurK1;
       int [] K1= new int[longeurK1];
       int [] K2 = new int[longeurK2];
       
        for (int i = 0; i < longeurK1; i++) {
            
            K1[i]=A[i];
        }
        
        for (int i=longeurK1 ; i < taille; i++) {
            
            K2[i-longeurK1]=A[i];
            
        }
        list.add(K1);
        list.add(K2);
        return list;
    }
    
    public static  int [] Et(int [] A,int [] B){
        int[] Tempo=new int[A.length];
        for (int i = 0; i < A.length; i++) {
        Tempo[i]= (A[i]==1&&B[i]==1)?1:0;
        }
        return Tempo;
    }
    
    public static  int [] Ou(int [] A,int [] B){
        int[] Tempo=new int[A.length];
        for (int i = 0; i < A.length; i++) {
        Tempo[i]= (A[i]==1||B[i]==1)?1:0;
        }
        return Tempo;
    }
    
    public static  int [] Ouexclusive(int [] A,int [] B){
        int[] Tempo=new int[A.length];
        for (int i = 0; i < A.length; i++) {
        Tempo[i]= (A[i]==B[i])?0:1;
        }
        return Tempo;
    }
    public static void main(String[] args) {
       Scanner ecrireposition = new Scanner(System.in);
       int index=0;
       int a = 0;
       int b = 0;
      int [] H = {6,5,2,7,4,1,3,0};
      
        for (int i = 0; i < H.length; i++) {
            System.out.println("L'élément à la position"+i+" est:"+H[i]);
        }
        
        Scanner valeurCle = new  Scanner(System.in);
        int [] K = {0,1,1,0,1,1,0,1};
      
       int[] tempo;
         
         K=permitation(K, H);
 
        
         int taille = K.length;
       int longeurK1 = K.length/2;
      int longeurK2 = taille-longeurK1;
       int [] K1= new int[longeurK1];
       int [] K2 = new int[longeurK2];
               
        K1=DivisionTabeau(K).get(0);
        K2=DivisionTabeau(K).get(1);
       
        System.out.println("Clé avec H appliqué : " +Arrays.toString(K));
        System.out.println("Première clé générée : " +Arrays.toString(K1));
        System.out.println("Deuxième clé générée : " +Arrays.toString(K2));        
      
        
        //Application des  opérations logiques sur les deux portion de la clé
        int[] K11=new int [K1.length];
        int [] K12= new int [K1.length];
        
       
        
        K11=Ouexclusive(K1, K2);
        K12=Et(K1, K2);
        
         
        
         
         //Application du decalage 
         tempo=new int[K11.length];
         for (int i = 2; i < K12.length; i++) {
            tempo[i-2]=K11[i];
        }
         tempo[K12.length-1]=K11[1];
         tempo[K11.length-2]=K11[0];
         K11=tempo;
         tempo=new int[K11.length];
         System.out.println("Première clé générée K1 : " +Arrays.toString(K11));
         
         a= K12[K12.length-1];
         
         tempo[0]=a;
         System.out.println("Mot de gauche K1: " +Arrays.toString(K11));
         for (int i = 0; i < K12.length-1; i++) {
            tempo[i+1]=K12[i];
        }
      K12=tempo;
      
       System.out.println("Deuxième clé générée K2 : " +Arrays.toString(K12));
       
       
       
       
       //Cryptage du mot
       
       
       //initialisation valeurs
       
       int [] mot = {0,1,1,0,1,1,1,0};
       int [] pi = {4,6,0,2,7,3,1,5};
       
       
       //application de la fonction de permutation et Round 1
        mot=permitation(mot, pi);
       System.out.println("Mot : " +Arrays.toString(mot));
       int[] Go,G1; //G0 est le premier G0, G1
       int[] Do,D1; 
       int [] p={2,0,1,3};
       
        Go=DivisionTabeau(mot).get(0);
        Do=DivisionTabeau(mot).get(1);
        
        
        System.out.println("Mot de gauche Go: " +Arrays.toString(Go));
        System.out.println("Mot de droite Do: " +Arrays.toString(Do));
  
        D1=Ouexclusive(permitation(Go, p), K11);
        G1=Ouexclusive(Do, Ou(Go, K11));
        
       System.out.println("Mot de gauche G1: " +Arrays.toString(G1));
        System.out.println("Mot de droite D1: " +Arrays.toString(D1));
      
        //Application d ela permutaion et Round 2
        
        int [] D2,G2;
        
        
        D2 = Ouexclusive((permitation(G1, p)), K12);
        G2 = Ouexclusive(D1, Ou(G1, K12));
        System.out.println("Mot de gauche G2: " +Arrays.toString(G2));
        System.out.println("Mot de droite D2: " +Arrays.toString(D2));
        
        //Concatenation de G2 et D2
        
        int [] C = new int [D2.length+G2.length];
        
        System.arraycopy(G2,0, C, 0, G2.length);
        System.arraycopy(D2,0, C, G2.length, D2.length);
        
        System.out.println("C = "+Arrays.toString(C));
        tempo=new int[pi.length];
        for (int i = 0; i < pi.length; i++) {
            int j=0;
            boolean bl=false;
            do{
                if(pi[j]==i){
                    bl=true;
                }
                else j++;
            }while(!bl);
            tempo[i]=j;
        }
        int[] pi1=tempo;
        
        int [] inversePi= new int [pi.length];
        
        System.out.println("pi1 = "+Arrays.toString(pi1));
        
        C= permitation(C, pi1);
         System.out.println("Mot Crypter = "+Arrays.toString(C));
        
        
    }
   
}