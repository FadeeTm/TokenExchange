
  function changeColorSell(btn) {
    btn.style.backgroundColor = "#E18056";
    document.getElementById('buy').style.backgroundColor = '#D6D5D1';
    document.getElementById('calc').value = 'CALCULATE SELLING';

    for (let i = 0; i < 8; i++) {
      elem = document.getElementById('l'+i);
      if (elem.checked) {
      elem.value = "1";
      }
      else elem.value = "0";
      }
  }

  function changeColorBuy(btn) {
    btn.style.backgroundColor = "#E18056";
    document.getElementById('sell').style.backgroundColor = '#D6D5D1';
    document.getElementById('calc').value = 'CALCULATE BUYING';

    for (let i = 0; i < 8; i++) {
      elem = document.getElementById('l'+i);
      if (elem.checked) {
      elem.value = "1";
      }
      else elem.value = "0";
      }
  }
