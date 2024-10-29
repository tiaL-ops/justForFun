import React, { useState } from 'react';
import { Pie } from 'react-chartjs-2';
import 'chart.js/auto';

function App() {
  const [income, setIncome] = useState(0);

  const categories = [
    { name: 'Education & Supplies', percentage: 30, color: '#4CAF50' },
    { name: 'Savings', percentage: 15, color: '#2196F3' },
    { name: 'Transportation', percentage: 10, color: '#FF9800' },
    { name: 'Food & Snacks Outside Dining Hall', percentage: 10, color: '#9C27B0' },
    { name: 'Entertainment & Social Activities', percentage: 20, color: '#FF5722' },
    { name: 'Health & Wellness', percentage: 5, color: '#00BCD4' },
    { name: 'Miscellaneous', percentage: 10, color: '#607D8B' },
  ];

  const calculateAllocation = (percentage) => ((income * percentage) / 100).toFixed(2);

  const data = {
    labels: categories.map((category) => category.name),
    datasets: [
      {
        data: categories.map((category) => category.percentage),
        backgroundColor: categories.map((category) => category.color),
        borderWidth: 2,
        hoverBorderColor: '#fff',
        hoverBorderWidth: 3,
      },
    ],
  };

  const options = {
    plugins: {
      legend: {
        display: true,
        position: 'right',
        labels: {
          font: { size: 14 },
          color: '#333',
          usePointStyle: true,
          padding: 15,
        },
      },
      tooltip: {
        callbacks: {
          label: (tooltipItem) => {
            const category = categories[tooltipItem.dataIndex];
            return `${category.name}: $${calculateAllocation(category.percentage)} (${category.percentage}%)`;
          },
        },
      },
    },
    animation: {
      animateScale: true,
      animateRotate: true,
    },
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>College Budget Planner</h1>

      {/* Banner-style Tips Section */}
      <div style={styles.tipsSection}>
        <h3 style={styles.tipsHeader}>Essential Budgeting Tips</h3>
        <ul style={{ listStyleType: 'none', paddingLeft: '0', marginTop: '10px' }}>
          <li style={tipStyle}>
            <span style={iconStyle}>💡</span>
            <strong>Understand Wants vs. Needs:</strong> Focus on needs first to avoid impulse spending!
          </li>
          <li style={tipStyle}>
            <span style={iconStyle}>💰</span>
            <strong>Save a Little Each Month:</strong> Even $10 monthly grows your savings.
          </li>
          <li style={tipStyle}>
            <span style={iconStyle}>🕒</span>
            <strong>Wait Before You Buy:</strong> Sleeping on a decision helps avoid impulse buys.
          </li>
          <li style={tipStyle}>
            <span style={iconStyle}>🎟️</span>
            <strong>Use Student Discounts:</strong> Many shops and services offer student discounts—just ask!
          </li>
          <li style={tipStyle}>
            <span style={iconStyle}>🍿</span>
            <strong>Find Free Fun:</strong> Check out campus events for entertainment without breaking the bank.
          </li>
          <li style={tipStyle}>
            <span style={iconStyle}>📅</span>
            <strong>Look Ahead:</strong> Plan ahead for larger expenses like textbooks to balance your budget.
          </li>
        </ul>
      </div>

      {/* Call-to-Action for Monthly Income */}
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <h2 style={styles.subHeader}>Enter Stipend to Check!</h2>
        <input
          type="number"
          value={income}
          onChange={(e) => setIncome(e.target.value)}
          placeholder="e.g., 500"
          style={styles.input}
        />
      </div>

      {/* Pie chart for budget allocation */}
      <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '30px' }}>
        <div style={{ width: '300px' }}>
          <Pie data={data} options={options} />
        </div>
      </div>

      {/* Display allocation breakdown */}
      <h3 style={styles.subHeader}>Budget Breakdown</h3>
      <ul style={{ listStyleType: 'none', paddingLeft: '0', fontSize: '16px', color: '#fff' }}>
        {categories.map((category, index) => (
          <li key={index} style={{ ...tipStyle, backgroundColor: 'transparent', boxShadow: 'none', textAlign: 'center' }}>
            <strong style={{ color: category.color }}>{category.name}:</strong> ${calculateAllocation(category.percentage)}
          </li>
        ))}
      </ul>
    </div>
  );
}

// Styles for layout and colors
const styles = {
  container: {
    fontFamily: 'Arial, sans-serif',
    maxWidth: '600px',
    margin: 'auto',
    padding: '20px',
    backgroundColor: '#800000',
    borderRadius: '10px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
  },
  header: {
    textAlign: 'center',
    color: '#FFFFFF',
    fontSize: '2em',
    fontWeight: 'bold',
  },
  tipsSection: {
    backgroundColor: '#ffe6e6',
    padding: '15px 20px',
    borderRadius: '10px',
    marginBottom: '20px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
  },
  tipsHeader: {
    color: '#800000',
    textAlign: 'center',
  },
  subHeader: {
    color: '#FFFFFF',
    textAlign: 'center',
    fontSize: '1.5em',
  },
  input: {
    padding: '10px',
    marginTop: '10px',
    borderRadius: '5px',
    border: '1px solid #ccc',
    fontSize: '16px',
    width: '150px',
    textAlign: 'center',
  },
};

// Styles for individual tips and icons
const tipStyle = {
  margin: '10px 0',
  padding: '10px',
  backgroundColor: '#ffffff',
  borderRadius: '8px',
  boxShadow: '0 2px 5px rgba(0, 0, 0, 0.1)',
  display: 'flex',
  alignItems: 'center',
};

const iconStyle = {
  fontSize: '24px',
  marginRight: '10px',
};

export default App;
