const dadosDoGrafo = {
  "layout": {
    "width": 650,
    "height": 500
  },
  "nos": [
    {
      "id": "A",
      "x": 100,
      "y": 100
    },
    {
      "id": "B",
      "x": 250,
      "y": 100
    },
    {
      "id": "C",
      "x": 400,
      "y": 100
    },
    {
      "id": "D",
      "x": 550,
      "y": 100
    },
    {
      "id": "E",
      "x": 100,
      "y": 250
    },
    {
      "id": "F",
      "x": 250,
      "y": 250
    },
    {
      "id": "G",
      "x": 400,
      "y": 250
    },
    {
      "id": "H",
      "x": 550,
      "y": 250
    },
    {
      "id": "I",
      "x": 100,
      "y": 400
    },
    {
      "id": "J",
      "x": 250,
      "y": 400
    },
    {
      "id": "K",
      "x": 400,
      "y": 400
    },
    {
      "id": "L",
      "x": 550,
      "y": 400
    }
  ],
  "arestas": [
    {
      "source": "A",
      "target": "B",
      "label": "clear_road",
      "peso": 0
    },
    {
      "source": "B",
      "target": "C",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "C",
      "target": "D",
      "label": "clear_road",
      "peso": 0
    },
    {
      "source": "E",
      "target": "F",
      "label": "clear_road",
      "peso": 0
    },
    {
      "source": "F",
      "target": "G",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "G",
      "target": "H",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "I",
      "target": "J",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "J",
      "target": "K",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "K",
      "target": "L",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "A",
      "target": "E",
      "label": "clear_road",
      "peso": 0
    },
    {
      "source": "E",
      "target": "I",
      "label": "clear_road",
      "peso": 0
    },
    {
      "source": "B",
      "target": "F",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "F",
      "target": "J",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "C",
      "target": "G",
      "label": "clear_road",
      "peso": 0
    },
    {
      "source": "G",
      "target": "K",
      "label": "obstructed_road",
      "peso": 5
    },
    {
      "source": "D",
      "target": "H",
      "label": "clear_road",
      "peso": 0
    },
    {
      "source": "H",
      "target": "L",
      "label": "clear_road",
      "peso": 0
    }
  ]
};
