// JobRecommendationGUI.java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*; 
import java.io.*;

public class JobRecommendationGUI {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Smart Job Recommendation System");
        frame.setSize(800, 500);  // Bigger window
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel label = new JLabel("Enter your skills (comma separated):");
        JTextField skillField = new JTextField(40);  // Wider input box
        JButton button = new JButton("Get Recommendations");

        // Bigger output area
        JTextArea resultArea = new JTextArea(20, 60); // more rows & columns
        resultArea.setEditable(false);
        resultArea.setFont(new Font("Monospaced", Font.PLAIN, 16)); // bigger font
        JScrollPane scrollPane = new JScrollPane(resultArea);

        // Panel with proper layout
        JPanel topPanel = new JPanel(new FlowLayout());
        topPanel.add(label);
        topPanel.add(skillField);
        topPanel.add(button);

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.add(topPanel, BorderLayout.NORTH);
        mainPanel.add(scrollPane, BorderLayout.CENTER);

        frame.add(mainPanel);
        frame.setVisible(true);

        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String skills = skillField.getText().trim();
                if (skills.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please enter skills!");
                    return;
                }
                try {
                    // Call Python script
                    ProcessBuilder pb = new ProcessBuilder("python", "smart_job_recommend.py");
                    Process p = pb.start();

                    // Send skills input to Python
                    BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
                    writer.write(skills + "\n");
                    writer.flush();
                    writer.close();

                    // Read Python output
                    BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
                    String line;
                    resultArea.setText("");
                    while ((line = reader.readLine()) != null) {
                        resultArea.append(line + "\n");
                    }
                    reader.close();

                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        });
    }
}
