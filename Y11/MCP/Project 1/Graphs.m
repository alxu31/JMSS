function rocket_ode()
    % Constants
    G = 6.6743*10^(-11);    % gravitational constant
    Mearth = 5.972*10^24;       % mass of Earth (kg)
    Mmars = 6.39*10^23;        % mass of Mars (kg)
    Rmars = 3.3895e6;          % radius of Mars (m)
    Rearth = 6371000;           % radius of Earth (m)
    d_earth_mars = 54.6e9;  % distance between Earth and Mars (m)
    Mejection = 2000;              % mass ejection rate (kg/s)
    Minitial = 100000;            % initial rocket mass (kg)
    Vejection = 50000;             % mass ejection velocity (m/s)
    
    % force of thrust
    function thr = thrust(t)
        if t <= 35
            thr = Mejection*Vejection;
        else
            thr = 0;
        end
    end
    

    % instantaneous mass of rocket
    function m = mass(t)
        if t <= 35
            m = Minitial - Mejection*t;
        else
            m = Minitial - Mejection*35;
        end
    end
    
    function dydt = ode(t, y)
        r = y(1);
        v = y(2);
        m = mass(t);
        thr = thrust(t);
        % Define the ODE function
        acceleration = thr/m - G*Mearth/(r+Rearth)^2 + G*Mmars/(d_earth_mars-r+Rmars)^2;
        
        dydt = [v; acceleration];
    end
    
    % Initial conditions
    y0 = [0; 0];   
    tspan = [0 100]; %Change (35, 100, 1000000)
    
    % Solve the ODE using ode45
    [t, y] = ode45(@ode, tspan, y0);
    
    % Extract solution
    r = y(:, 1);       % r(t)
    v = y(:, 2);       % r'(t)
    
    % calculating acceleration graph
    a = zeros(size(t));
    mv = zeros(size(t));
    thr = zeros(size(t));
    for i = 1:length(t)
        mv(i) = mass(t(i));
        thr(i) = thrust(t(i)); % Calculate thrust at time t(i)
        a(i) =  thr(i)/mv(i) - G*Mearth/(r(i)+Rearth)^2 + G*Mmars/(d_earth_mars-r(i)+Rmars)^2;
        r(i)
    end
    
    
    % Find the index where rocket reaches Mars
    index_mars = find(r >= d_earth_mars, 1);
    
    % Plotting only until the rocket reaches Mars
    if ~isempty(index_mars)
        t_plot = t(1:index_mars);
        r_plot = r(1:index_mars);
        v_plot = v(1:index_mars);
        a_plot = a(1:index_mars);
    else
        t_plot = t;
        r_plot = r;
        v_plot = v;
        a_plot = a;
    end
    
    % Plotting
    figure;
    
    % Displacement
    subplot(4, 1, 1);
    plot(t_plot, r_plot, 'b', 'LineWidth', 1.5);
    xlabel('Time (s)');
    ylabel('Position (m)');
    title('Displacement');
    grid on;

    % Velocity
    subplot(4, 1, 2);
    plot(t_plot, v_plot, 'r', 'LineWidth', 1.5);
    xlabel('Time (s)');
    ylabel('Velocity (m/s)');
    title('Velocity');
    grid on;

    % Acceleration 
    subplot(4, 1, 3);
    plot(t_plot, a_plot, 'g', 'LineWidth', 1.5);
    xlabel('Time (s)');
    ylabel('Acceleration (m/s^2)');
    title('Acceleration');
    grid on;
    

    % Print position, time, velocity, and acceleration (wrong, but close)
    if ~isempty(index_mars)
        fprintf('Rocket reached Mars at:\n');
        fprintf('Time: %.2f seconds\n', t(index_mars));
        fprintf('Position: %.2f meters\n', r(index_mars));
        fprintf('Velocity: %.2f m/s\n', v(index_mars));
        fprintf('Acceleration: %.2f m/s^2\n', a(index_mars));
    else
        fprintf('Rocket did not reach Mars within the simulation time.\n');
    end
end
