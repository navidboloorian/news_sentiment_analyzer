import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const data = await d3.csv("../data.csv");

const sentimentToLabel = (sentiment) => {
  if (sentiment > 2) {
    return "Positive";
  } else if (sentiment > 1) {
    return "Neutral";
  } else {
    return "Negative";
  }
};

const createGraph = (source) => {
  const width = 750;
  const height = 750;
  const margin = { bottom: 50, top: 30, right: 30, left: 30 };

  const paddedWidth = width + margin.left + margin.right;
  const paddedHeight = height + margin.bottom + margin.top;

  const svg = d3
    .select("#graph-wrapper")
    .append("svg")
    .attr("width", paddedWidth)
    .attr("height", paddedHeight)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  const tooltip = d3
    .select("#graph-wrapper")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

  const mouseover = function (event, d) {
    tooltip.style("opacity", 1);
  };

  const mousemove = function (event, d) {
    tooltip
      .html(
        `
        <p class='tooltip-headline'>${d.headline}</p>
        <p>Sentiment: ${
          Math.round(d.sentiment * 1000) / 1000
        } (${sentimentToLabel(d.sentiment)})</p>
      `
      )
      .style("left", event.x + "px")
      .style("top", event.y + "px");
  };

  const mouseleave = function (event, d) {
    tooltip.style("opacity", 0);
  };

  const xScale = d3
    .scaleUtc()
    .domain(
      d3.extent(
        data.filter((row) => row.source === source),
        (d) => new Date(d.date)
      )
    )
    .range([50, width]);

  const yScale = d3.scaleLinear().domain([0, 3]).range([height, 0]);

  const xAxis = d3
    .axisBottom(xScale)
    .ticks(d3.utcDay.every(1))
    .tickFormat((d) => d.toLocaleDateString("en-US"));
  const yAxis = d3.axisLeft(yScale);

  svg.append("g").attr("transform", `translate(0, ${height})`).call(xAxis);
  svg.append("g").call(yAxis);

  svg
    .append("g")
    .selectAll("circle")
    .data(data.filter((row) => row.source === source))
    .enter()
    .append("circle")
    .attr("cx", function (d) {
      return xScale(new Date(d.date));
    })
    .attr("cy", function (d) {
      return yScale(d.sentiment);
    })
    .attr("r", 10)
    .attr("stroke", "black")
    .style("fill", function (d) {
      return d.subject === "Republicans" ? "#e81b23" : "#00aef3";
    })
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave);
};

createGraph("fox");
