import React from 'react';
import * as d3 from 'd3';

const Analytics = () => {
  const data = [
    // Your data for the chart
  ];

  // Create a scale for the x-axis
  const x = d3.scaleBand().range([0, 500]).domain(data.map((d) => d.month)).padding(0.2);

  // Create a scale for the y-axis
  const y = d3.scaleLinear().domain([0, 500]).range([300, 0]);

  // Create the x-axis
  const xAxis = d3.axisBottom(x);

  // Create the y-axis
  const yAxis = d3.axisLeft(y);

  // Append the SVG element
  const svg = d3.select('body').append('svg').attr('width', 500).attr('height', 300);

  // Append the x-axis to the SVG
  svg.append('g').attr('transform', 'translate(0, 300)').call(xAxis);

  // Append the y-axis to the SVG
  svg.append('g').call(yAxis);

  // Add the bars to the chart
  svg
    .selectAll('bars')
    .data(data)
    .enter()
    .append('rect')
    .attr('x', (d) => x(d.month))
    .attr('y', (d) => y(d.value))
    .attr('width', x.bandwidth())
    .attr('height', (d) => 300 - y(d.value))
    .attr('fill', '#d04a35');

  return <div id="chart"></div>;
};

export default Analytics;
