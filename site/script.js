import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const data = await d3.csv("../data.csv");

const createGraph = (source) => {
  const graphWrapper = document.querySelector("#graph-wrapper");
  const svg = document.createElement("svg");

  const width = 500;
  const height = 500;

  const xAxis = d3.scaleLinear();

  d3.select(svg)
    .selectAll("circle")
    .data(data.filter((row) => row.source === source))
    .join("circle");

  graphWrapper.appendChild(svg);
};

createGraph("fox");
