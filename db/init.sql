-- viewer_recipe table
INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Abdominaux', 'core', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'core');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pectoraux', 'pectorals', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'pectorals');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Trapèzes', 'trapezoid', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'trapezoid');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Cervicales', 'cervical', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'cervical');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Epaules', 'deltoids', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'deltoids');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Biceps', 'biceps', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'biceps');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Coudes', 'elbow', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'elbow');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Avant Bras', 'forearm', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'forearm');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Poignets', 'wrist', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'wrist');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Mains', 'hand', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hand');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pieds', 'foot', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'foot');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Chevilles', 'ankle', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'ankle');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tibias', 'tibia', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'tibia');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Genoux', 'knee', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'knee');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tenseurs du Fascia Lata', 'quadz2', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz2');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Quadriceps', 'quadz1', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz1');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Obliques', 'oblic', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'oblic');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Adducteurs', 'adductors', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'adductors');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Rhomboides', 'rhomboids', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'rhomboids');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Triceps', 'triceps', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'triceps');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Dorsaux', 'lats', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'lats');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Lombaires', 'lumbar', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'lumbar');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Hanches', 'hips', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hips');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Fessiers', 'glutes', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'glutes');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Ischios', 'hamstrings', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hamstrings');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Mollets', 'calf', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'calf');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tendon D''achille', 'achille', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'achille');
