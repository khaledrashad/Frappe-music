let currentPage = 1;
const pageSize = 10;

async function loadSongs(page, name) {
    if (page < 1) return;

    const encodedName = encodeURIComponent(name);

    const response = await fetch(`/api/method/music_app.www.specificArtist.get_paginated_songs?page_number=${page}&page_size=${pageSize}&name=${encodedName}`);
    const data = await response.json();
    const { songs, total_songs, page_number, page_size } = data.message;

    console.log(songs, total_songs);
    currentPage = page_number;

    const songsContainer = document.getElementById('songs-container');
    songsContainer.innerHTML = '';

    songs.forEach(song => {
        const songCard = `
            <div class="col-md-6">
                <div class="songCard w-100 border border-3 p-2 m-2 text-center">
                    <img src="${song.song_image}" alt="Image of ${song.name}" class="w-75 img-fluid">
                    <h4 class="m-0 p-0">${song.artist}</h4>
                    <h3 class="m-0 p-0 text-info">${song.name}</h3>
                </div>
            </div>
        `;
        songsContainer.innerHTML += songCard;
    });

    const totalPages = Math.ceil(total_songs / page_size);
    document.getElementById('page-info').innerText = `Page ${page_number} of ${totalPages}`;
    document.getElementById('prev-page').disabled = page_number === 1;
    document.getElementById('next-page').disabled = page_number === totalPages;
}

function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

document.addEventListener('DOMContentLoaded', function() {
    const artistName = getUrlParameter('name');

    if (artistName) {
        loadSongs(currentPage, artistName);
    } else {
        console.error('Artist name parameter is missing in the URL.');
    }
});
