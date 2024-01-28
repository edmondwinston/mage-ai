import { test as base, expect } from '@playwright/test';

export const test = base.extend<{ page: void; failOnClientError: boolean; }>({
  page: async ({ page, failOnClientError }, use) => {
    const pageErrors: Error[] = [];
    page.addListener('pageerror', (error) => {
      pageErrors.push(error);
    });

    await page.goto('/sign-in');
    await page.getByPlaceholder('Email').click();
    await page.getByRole('textbox').first().fill('admin@admin.com');
    await page.getByRole('textbox').first().press('Tab');
    await page.locator('input[type="password"]').fill('admin');
    await page.locator('input[type="password"]').press('Enter');

    /*
     * Wait for redirected page, which can be /overview (if at least 1 pipeline run exists)
     * or /pipelines (if no pipeline runs exist), to load after signing in.
     */
    await expect(page.getByRole('button', { name: 'New' })).toBeVisible({ timeout: 10000 });

    // Use subsequent tests.
    await use(page);

    if (failOnClientError) {
      expect(pageErrors).toHaveLength(0);
    }
  },
});

export { expect };
