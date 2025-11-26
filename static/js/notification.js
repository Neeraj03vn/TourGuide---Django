const notificationContainer = document.getElementById('notification-container');

// Function to show notification
function showNotification(message) {
  const notification = document.createElement('div');
  notification.classList.add('notification');
  notification.innerHTML = `
    <span>${message}</span>
    <button>Close</button>
  `;
  notificationContainer.appendChild(notification);

  // Close notification on button click
  notification.querySelector('button').addEventListener('click', () => {
    notification.remove();
  });
}

