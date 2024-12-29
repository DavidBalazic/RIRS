import {defineConfig} from 'vitest/config'
import {sveltekit} from '@sveltejs/kit/vite'
import {svelteTesting} from '@testing-library/svelte/vite'

export default defineConfig({
  plugins: [sveltekit(), svelteTesting()],
  test: {
    coverage: {
      reporter: ['text', 'lcov'],
      reportsDirectory: './coverage',
    },
	  globals: true,
    environment: 'jsdom',
    setupFiles: ['./vitest-setup.js'],
  },
})