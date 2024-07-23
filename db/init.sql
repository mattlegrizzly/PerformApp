-- viewer_recipe table
INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Abdominaux', 'core', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'core');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pectoraux', 'pectorals', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'pectorals');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pectoral Droit', 'pectorals-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'pectorals-right');
INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pectoral Gauche', 'pectorals-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'pectorals-left');

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
SELECT 'Epaule Gauche', 'deltoids-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'deltoids-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Epaule Droite', 'deltoids-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'deltoids-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Biceps', 'biceps', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'biceps');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Biceps Gauche', 'biceps-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'biceps-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Biceps Droit', 'biceps-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'biceps-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Coudes', 'elbow', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'elbow');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Coude Gauche', 'elbow-left', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'elbow-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Coude Droit', 'elbow-right', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'elbow-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Avant Bras', 'forearm', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'forearm');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Avant Bras Gauche', 'forearm-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'forearm-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Avant Bras Droit', 'forearm-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'forearm-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Poignets', 'wrist', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'wrist');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Poignet Droit', 'wrist-right', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'wrist-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Poignet Gauche', 'wrist-left', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'wrist-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Mains', 'hand', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hand');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Main Gauche', 'hand-left', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hand-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Main Droite', 'hand-right', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hand-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pieds', 'foot', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'foot');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pied Gauche', 'foot-left', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'foot-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Pied Droit', 'foot-right', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'foot-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Chevilles', 'ankle', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'ankle');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Cheville Droite', 'ankle-right', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'ankle-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Cheville Gauche', 'ankle-left', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'ankle-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tibias', 'tibia', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'tibia');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tibia Gauche', 'tibia-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'tibia-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tibia Droit', 'tibia-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'tibia-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Genoux', 'knee', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'knee');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Genou Gauche', 'knee-left', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'knee-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Genou Droit', 'knee-right', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'knee-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tenseurs du Fascia Lata', 'quadz2', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz2');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tenseur du Fascia Lata Droit', 'quadz2-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz2-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tenseur du Fascia Lata Gauche', 'quadz2-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz2-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Quadriceps', 'quadz1', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz1');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Quadriceps Gauche', 'quadz1-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz1-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Quadriceps Droit', 'quadz1-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'quadz1-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Obliques', 'oblic', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'oblic');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Oblique Gauche', 'oblic-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'oblic-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Oblique Droit', 'oblic-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'oblic-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Adducteurs', 'adductors', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'adductors');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Adducteur Droit', 'adductors-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'adductors-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Adducteur Gauche', 'adductors-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'adductors-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Triceps', 'triceps', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'triceps');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Triceps Gauche', 'triceps-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'triceps-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Triceps Droit', 'triceps-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'triceps-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Dorsaux', 'lats', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'lats');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Grand Dorsal Droit', 'lats-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'lats-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Grand Dorsal Gauche', 'lats-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'lats-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Lombaires', 'lumbar', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'lumbar');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Hanches', 'hips', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hips');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Hanche Gauche', 'hips-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hips-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Hanche Droite', 'hips-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hips-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Fessiers', 'glutes', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'glutes');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Fessier Droit', 'glutes-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'glutes-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Fessier Gauche', 'glutes-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'glutes-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Ischios Jambier', 'hamstrings', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hamstrings');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Ischio Jambier Droit', 'hamstrings-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hamstrings-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Ischio Jambier Gauche', 'hamstrings-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'hamstrings-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Mollets', 'calf', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'calf');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Mollet Droit', 'calf-right', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'calf-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Mollet Gauche', 'calf-left', 'MU', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'calf-left');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tendon D''achille', 'achille', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'achille');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tendon D''achille Droit', 'achille-right', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'achille-right');

INSERT INTO "exercise_workzone" (name, code, zone, created_at, updated_at)
SELECT 'Tendon D''achille Gauche', 'achille-left', 'AR', current_timestamp, current_timestamp
WHERE NOT EXISTS (SELECT 1 FROM "exercise_workzone" WHERE code= 'achille-left');
