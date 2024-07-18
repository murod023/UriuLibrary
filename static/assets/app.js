// Обработка нажатия на бургер-меню
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');
const overlay = document.querySelector('.overlay');

burger.addEventListener('click', () => {
    nav.classList.toggle('active');
    burger.classList.toggle('active');
    overlay.classList.toggle('active');
});

// Обработка нажатия на оверлей для закрытия меню и оверлея
overlay.addEventListener('click', () => {
    nav.classList.remove('active');
    burger.classList.remove('active');
    overlay.classList.remove('active');
});


// Инициализация библиотеки pdf.js
const pdfjsLib = window['pdfjs-dist/build/pdf'];
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.4.456/pdf.worker.min.js';

// Функция для создания карточки PDF
function createCard(cardElement) {
    const url = cardElement.dataset.url;
    const title = cardElement.querySelector('.card-title').innerText.trim();

    const img = cardElement.querySelector('img');
    img.alt = title;

    const downloadButton = cardElement.querySelector('.download-button');
    downloadButton.onclick = () => window.location.href = url;

    fetch(url).then(response => response.arrayBuffer()).then(arrayBuffer => {
        pdfjsLib.getDocument(arrayBuffer).promise.then(pdfDoc => {
            pdfDoc.getPage(1).then(page => {
                const scale = 1.5;
                const viewport = page.getViewport({ scale: scale });

                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d');
                canvas.height = viewport.height;
                canvas.width = viewport.width;

                page.render({ canvasContext: context, viewport: viewport }).promise.then(() => {
                    img.src = canvas.toDataURL();
                });
            });
        });
    });
}

function showWindow(windowId) {
    // Скрыть все окна
    var windows = document.querySelectorAll('.window');
    windows.forEach(function(window) {
        window.style.display = 'none';
    });

    // Показать выбранное окно
    var selectedWindow = document.getElementById(windowId);
    selectedWindow.style.display = 'block';
}

var acc = document.getElementsByClassName("accordion");
for (var i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}

// Применение функции createCard ко всем элементам с классом 'card'
const cards = document.querySelectorAll('.card');
cards.forEach(createCard);
