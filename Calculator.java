
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class Calculator implements ActionListener{
	
	
	JFrame frame;
	JTextField textfield;
	JButton[] numbers = new JButton[10];
	JButton[] operations = new JButton[8];
	JButton add, subtract, multiply, divide, decimal, equals, delete, clear;
	JPanel panel;
	
	Font font = new Font("Ink Free", Font.BOLD, 30);
	double num1 = 0;
	double num2 = 0;
	double res = 0;
	char operator;
	
	Calculator(){
		frame = new JFrame("calculator");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(420, 550);
		frame.setLayout(null);
		
		textfield = new JTextField();
		textfield.setBounds(50, 25, 300, 50);
		textfield.setFont(font);
		textfield.setEditable(false);
		
		add = new JButton("+");
		subtract = new JButton("-");
		multiply = new JButton("*");
		divide = new JButton("/");
		decimal = new JButton(".");
		equals = new JButton("=");
		delete = new JButton("del");
		clear = new JButton("clr");
		
		operations[0] = add;
		operations[1] = subtract;
		operations[2] = multiply;
		operations[3] = divide;
		operations[4] = decimal;
		operations[5] = equals;
		operations[6] = delete;
		operations[7] = clear;
		
		for(int i =0;i<8;i++) {
			operations[i].addActionListener(this);
			operations[i].setFont(font);
			operations[i].setFocusable(false);
		}

		for(int i =0;i<10;i++) {
			numbers[i] = new JButton(String.valueOf(i));
			numbers[i].addActionListener(this);
			numbers[i].setFont(font);
			numbers[i].setFocusable(false);

		}
		delete.setBounds(50,430,125,50);
		clear.setBounds(225,430,125,50);

		panel = new JPanel();
		panel.setBounds(50, 100, 300, 300);
		panel.setLayout(new GridLayout(4,4,10,10));
		
		
		panel.add(numbers[1]);
		panel.add(numbers[2]);
		panel.add(numbers[3]);
		panel.add(add);
		panel.add(numbers[4]);
		panel.add(numbers[5]);
		panel.add(numbers[6]);
		panel.add(subtract);
		panel.add(numbers[7]);
		panel.add(numbers[8]);
		panel.add(numbers[9]);
		panel.add(multiply);
		panel.add(decimal);
		panel.add(numbers[0]);
		panel.add(equals);
		panel.add(divide);
		
		frame.add(panel);
		frame.add(delete);
		frame.add(clear);

		;
		frame.add(textfield);		
		frame.setVisible(true);
	}

	public static void main(String[] args) {
		Calculator calc = new Calculator();

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		for(int i=0;i<10;i++) {
			if(e.getSource() == numbers[i]) {
				textfield.setText(textfield.getText().concat(String.valueOf(i)));
			}
		}
		if(e.getSource()==decimal) {
			textfield.setText(textfield.getText().concat("."));
		}
		if(e.getSource()==add) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='+';
			textfield.setText("");
		}
		if(e.getSource()==subtract) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='-';
			textfield.setText("");
		}
		if(e.getSource()==multiply) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='*';
			textfield.setText("");
		}
		if(e.getSource()==divide) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='/';
			textfield.setText("");
		}
		if(e.getSource()==equals) {
			num2=Double.parseDouble(textfield.getText());

			switch(operator) {
			case'+':
				res=num1+num2;
				break;
			case'-':
				res=num1-num2;
				break;
			case'*':
				res=num1*num2;
				break;
			case'/':
				res=num1/num2;
				break;
			}
			textfield.setText(String.valueOf(res));
			num1=res;
		}
		if(e.getSource()==clear) {
			textfield.setText("");
		}
		if(e.getSource()==delete) {
			String string = textfield.getText();
			textfield.setText("");
			for(int i=0;i<string.length()-1;i++) {
				textfield.setText(textfield.getText()+string.charAt(i));
			}
		}
	}


		
}



