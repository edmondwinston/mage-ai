import { expect, test } from './base';

test('ensure `example_pipeline` runs smoothly', async ({ page }) => {
  await page.goto('/pipelines');
  await page.getByRole('link', { name: 'example_pipeline' }).click();
  await page.getByRole('button', { name: 'Run@once' }).click();
  await page.getByRole('button', { name: 'Run now' }).click();

  await expect(page.locator('#pipeline-triggers-row-0')).toContainText('running');
  await page.locator('#pipeline-triggers-row-0').getByRole('link').click();
  await expect(page.getByRole('button', { name: 'Running' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Done' })).toBeVisible();
  await page.getByRole('link', { name: 'example_pipeline' }).click();
  await expect(page.locator('#pipeline-triggers-row-0')).toContainText('completed');
});