import '@testing-library/jest-dom/vitest';
Object.defineProperty(global.Element.prototype, 'animate', {
    value: () => ({
      cancel: () => {},
      finish: () => {},
      play: () => {},
      pause: () => {},
    }),
  });
  