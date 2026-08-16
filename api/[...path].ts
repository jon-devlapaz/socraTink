// @ts-expect-error Vite generates this Flue runtime entry during `pnpm build`.
import { loadFlueNodeApplication } from '../dist/app.mjs';

let application = loadFlueNodeApplication();

export default {
	async fetch(request: Request) {
		const loaded = await application;
		const activity = loaded.enterActivity();
		try {
			return await loaded.fetch(request);
		} finally {
			activity.release();
		}
	},
};
