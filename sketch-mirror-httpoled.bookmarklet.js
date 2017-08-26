(() => {
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.target.parentElement.parentElement.className.indexOf('Artboard__item') === -1) {
        console.log(`found canvas update: ${mutation.target.src}`);

        const image = new Image();

        const render = () => {
          image.removeEventListener('load', render);

          const canvas = document.createElement('canvas');
          canvas.width = image.naturalWidth;
          canvas.height = image.naturalHeight;
          const context = canvas.getContext('2d');
          context.drawImage(image, 0, 0);

          canvas.toBlob((blob) => {
            console.log(`uploading image data`, blob);
            const formData = new FormData();
            formData.append('image', blob);
            const xhr = new XMLHttpRequest;
            xhr.open('POST', 'http://<your-raspberry-pi>.local:8080/');
            xhr.send(formData);
          });
        };

        image.addEventListener('load', render);
        image.src = mutation.target.src.replace('scale=2', 'scale=1');
      }
    });
  });

  observer.observe(document.body, {
    attributes: true,
    subtree: true,
    attributeFilter: ['src']
  });
})();