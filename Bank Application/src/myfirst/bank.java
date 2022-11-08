package myfirst;
import java.lang.*;
import java.util.*;
import java.math.*;



public class bank {
	
	public static void main(String[] args) 
	{
		
		int balance = 0;
		int deposit = 0;
		int withdraw = 0;
		String preTransactions = "";
		
		System.out.println("Welcome back NAME");
		System.out.println("BA0001");
		System.out.println("What would you like to do?");
		
		
		
		while (true)	
		{
			System.out.println("A: Check Balance");
			System.out.println("B: Deposit");
			System.out.println("C: Withdraw");
			System.out.println("D: Exit");

			Scanner sc = new Scanner(System.in);
			String user = sc.nextLine();
			
			if (user.equals("D"))
			{
				break;
			}
			
			else if (user.equals("A"))
			{
				System.out.println("You have: " + balance);
				preTransactions = "A";

			}
			
			else if (user.equals("B"))
			{
				System.out.println("Enter Amount");
				Scanner user_deposit = new Scanner(System.in);
				String userDeposit = user_deposit.nextLine();
				
				
				deposit = Integer.parseInt(userDeposit);
				balance = balance + deposit;
				preTransactions = "B";

			}
			
			else if (user.equals("C"))
			{
				System.out.println("Enter amount to withdraw: ");
				Scanner user_withdraw = new Scanner(System.in);
				String userWithraw = user_withdraw.nextLine();
				
				withdraw = Integer.parseInt(userWithraw);
				if (withdraw > balance)
				{
					System.out.println("Error, you don't have enough to take out!");
				}
				
				else if (withdraw < 0)
				{
					System.out.println("Please enter a positive number");
				}
				
				else
				{
				balance  = balance - withdraw;	
				preTransactions = "C";
				}
				
			}
			
			else
			{
				System.out.println("Please enter a valid option");
			}
			
			
			
		}

	
	     
	    

	}

}
